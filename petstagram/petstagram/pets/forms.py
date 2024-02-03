from django import forms

from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name','date_of_birth', 'personal_photo')


class PetDeleteForm(PetForm):
    # def __init__(self):
    #     super().__init__()
    #     self.fields['name'].disabled = True
    #     self.fields['date_of_birth'].disabled = True
    #     self.fields['personal_photo'].disabled = True

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


