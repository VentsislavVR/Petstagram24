from django import forms

from petstagram.core.form_mixin import ReadonlyFieldsFormMixin
from petstagram.photos.models import Photo

class PetPhotoBaseForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('photo','description',
                  'location','tagged_pets')





class PetPhotoCreateForm(PetPhotoBaseForm):
    pass
class PetPhotoEditForm(ReadonlyFieldsFormMixin,PetPhotoBaseForm):
    readonly_fields = ('photo','tagged_pets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

