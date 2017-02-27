from django.shortcuts import render


# Create your views here.

from schapen.models import Schapen
from schapen.forms import AddSchapen
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
import datetime
import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse



# view na login, alles met suffix bedrijf
@login_required
def bedrijf_index(request):
    today = datetime.datetime.today()
    huidige_gebruiker = request.user
    schapen_overzicht = Schapen.objects.filter(Q(einddatum__gt = today) | Q(einddatum__isnull = True )).order_by('intern_nummer')
    schapen_overzicht_pergebruiker = schapen_overzicht.filter(owner = huidige_gebruiker )
    context = {'schapen_overzicht':schapen_overzicht_pergebruiker}
    return render(request, 'bedrijf/index.html', context)

@login_required
def bedrijf_aanwezige_schapen(request):
    today = datetime.datetime.today()
    huidige_gebruiker = request.user
    schapen_overzicht = Schapen.objects.filter(Q(einddatum__gt = today) | Q(einddatum__isnull = True )).order_by('intern_nummer')
    schapen_overzicht_pergebruiker = schapen_overzicht.filter(owner = huidige_gebruiker )
    context = {'schapen_overzicht':schapen_overzicht_pergebruiker}
    return render(request, 'bedrijf/aanwezige_schapen.html', context)

@login_required
def bedrijf_alle_schapen(request):
    huidige_gebruiker = request.user
    schapen_overzicht = Schapen.objects.order_by('intern_nummer')
    schapen_overzicht_pergebruiker = schapen_overzicht.filter(owner = huidige_gebruiker )
    context = {'schapen_overzicht':schapen_overzicht_pergebruiker}
    return render(request, 'bedrijf/alle_schapen.html', context)

@login_required
def bedrijf_schaap_toevoegen(request):
    if request.method == "POST":
        form = AddSchapen(request.POST)
        if form.is_valid():
            formulier = form.save(commit=False)
            formulier.owner = request.user
            formulier.pub_datum = datetime.datetime.now()
            formulier.save()
            #schapen_overzicht = Schapen.objects.order_by('intern_nummer')
            #context = {'schapen_overzicht':schapen_overzicht}
            #return render(request, 'bedrijf/alle_schapen.html', context)
            return HttpResponseRedirect(reverse('schapen:bedrijf_schaap_toevoegen'))
    else:
        form = AddSchapen()
        return render(request, 'bedrijf/schaap_toevoegen.html',  {'form': form})

@login_required
def bedrijf_schaap_detail(request, id):
    schaap = get_object_or_404(Schapen, pk=id)
    form = AddSchapen()
    return render(request, 'bedrijf/schaap_detail.html', {'schapen': schaap, 'form': form})



class CustomModelForm(forms.ModelForm):
    """
    Sandboxes user data for each reference field pointing to an
    object with an "owner" field.
    """
    def __init__(self, request, *args, **kwargs):
        # cache the request object
        self.request = request
        init_result = super(CustomModelForm, self).__init__(*args, **kwargs)

        # go through each field in this ModelForm
        for field_name, field_widget in self.fields.iteritems():
            # find the model field definition
            model_field = getattr(self.Meta.model, field_name, None)
            if model_field:
                # check if it has a related model
                related_model = getattr(model_field.field, 'related_model', None)
                if related_model:
                    # check if it has an owner field
                    owner_field = getattr(related_model, 'owner', None)
                    if owner_field:
                        # filter field objects by owner = logged in user
                        field_widget.queryset = related_model.objects.filter(owner=request.user)

        return init_result
