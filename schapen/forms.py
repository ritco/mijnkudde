from django import forms
from django.forms import extras
from .models import Schapen
from django.forms.fields import DateField


#class AddSchapen(forms.ModelForm):
#
#    class Meta:
#        model = Schapen
#        exclude = ('user', )


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



class AddSchapen(CustomModelForm):
    pass
