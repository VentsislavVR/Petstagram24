from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic as views

from petstagram.core.view_mixins import OwnerRequiredMixin
from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import Photo
from django.contrib.auth import mixins as auth_mixins

class PetPhotoCreateView(auth_mixins.LoginRequiredMixin,views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = 'photos/create_photo.html'
    queryset = Photo.objects.all()\
    .prefetch_related('tagged_pets')
    def get_success_url(self):
        return reverse('photo  details', kwargs={
            'pk': self.object.pk
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.user = self.request.user
        return form

class PetPhotoDetailsView(auth_mixins.LoginRequiredMixin,views.DetailView):
    queryset = Photo.objects.all()\
        .prefetch_related('tagged_pets')\
        .prefetch_related('likes')\
        .prefetch_related('comments')

    template_name = 'photos/details_photo.html'


class PetPhotoEditView(OwnerRequiredMixin,views.UpdateView):
    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets')

    template_name = 'photos/edit_photo.html'
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse('details photo', kwargs={
            'pk': self.object.pk
        })




def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()

    return redirect('index')