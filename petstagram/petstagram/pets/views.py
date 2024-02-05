from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
def pet_add(request):
    pet_form = PetCreateForm(request.POST or None)
    if request.method == 'POST':

        if pet_form.is_valid():
            created_pet = pet_form.save()
            return redirect('pet_details', username='lenovo', pet_slug=created_pet.slug)

    context = {
        'form': pet_form,
    }
    return render(
        request,
        'pets/pet-add-page.html',
        context
    )


def pet_details(request, username, pet_slug):
    context = {
        "pet": Pet.objects.get(slug=pet_slug),
    }

    return render(
        request,
        'pets/pet-details-page.html',
        context
    )


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('pet_details', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'username': username,
        'pet': pet,

    }
    return render(
        request,
        'pets/pet-edit-page.html',
        context
    )


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

    form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        form.save()
        return redirect("index")

    context = {
        'form': form,
        'username': username,
        'pet': pet,
    }
    return render(
        request,
        'pets/pet-delete-page.html',
        context
    )
