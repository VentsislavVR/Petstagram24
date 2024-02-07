from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


def photo_add(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')


    context = {
        'form': form
    }
    return render(
        request,
        'photos/photo-add-page.html',
        context
    )


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.likes.count()
    comments = photo.comments.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }
    return render(
        request,
        'photos/photo-details-page.html',
        context
    )


def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('photo_details', pk=pk)
    context = {
        'form': form,
        'photo': photo
    }
    return render(
        request,
        'photos/photo-edit-page.html',
        context
    )

def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()

    return redirect('index')