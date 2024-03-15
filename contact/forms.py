from django import forms
from django.core.exceptions import ValidationError
from contact import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone',

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid')
        )
        return super().clean()
