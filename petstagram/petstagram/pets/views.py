from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from petstagram.core.view_mixins import OwnerRequiredMixin
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet
from django.contrib.auth import mixins as auth_mixins



class PetCreateView(OwnerRequiredMixin,views.CreateView):
    # model = Pet
    # fields = ("name", "date_of_birth", "personal_photo")
    form_class = PetCreateForm
    template_name = "pets/create_pet.html"

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": "lenovo",
            "pet_slug": self.object.slug,
        }
                       )
    # Todo figure out
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["initial"] = {'user':self.request.user}
    #     return kwargs

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.user = self.request.user
    #     return super().form_valid(form)
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.user = self.request.user
        return form


# FBV CREATE PET

# Create your views here.

# def pet_add(request):
#     pet_form = PetCreateForm(request.POST or None)
#     if request.method == "POST":
#
#         if pet_form.is_valid():
#             created_pet = pet_form.save()
#             return redirect("pet_details", username="lenovo", pet_slug=created_pet.slug)
#
#     context = {
#         "form": pet_form,
#     }
#     return render(
#         request,
#         "pets/create_pet.html",
#         context
#     )

class PetDetailsView(auth_mixins.LoginRequiredMixin,views.DetailView):
    # TODO: fix bad queries
    # model = Pet  # or query
    queryset = Pet.objects.all() \
        .prefetch_related("photo_set") \
        .prefetch_related("photo_set__likes") \
        .prefetch_related("photo_set__comments") \
        .prefetch_related("photo_set__tagged_pets")
    template_name = "pets/details_pet.html"
    # slug="pet_slug" # name of field in model
    slug_url_kwarg = "pet_slug"  # name of param in URL


# def pet_details(request, username, pet_slug):
#     context = {
#         "pet": Pet.objects.get(slug=pet_slug),
#     }
#
#     return render(
#         request,
#         "pets/details_pet.html",
#         context
#     )



class PetEditView(auth_mixins.LoginRequiredMixin,views.UpdateView):
    model = Pet  # or query Pet.objects.all()
    form_class = PetEditForm
    template_name = "pets/edit_pet.html"

    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = "lenovo"
        return context

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": self.request.GET.get("username"),
            "pet_slug": self.object.slug,
        }
                       )





# def pet_edit(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).get()
#     form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         return redirect("details pet", username=username, pet_slug=pet_slug)
#
#     context = {
#         "form": form,
#         "username": username,
#         "pet": pet,
#
#     }
#     return render(
#         request,
#         "pets/edit_pet.html",
#         context
#     )
class PetDeleteView(OwnerRequiredMixin,views.DeleteView):
    model = Pet
    form_class = PetDeleteForm

    template_name = "pets/delete_pet.html"

    slug_url_kwarg = "pet_slug"

    success_url = reverse_lazy("index")

    extra_context = {
        "username": "lenovo",
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = self.form_class(instance=self.object)
    #     context["form"] = form
    #     return context

# def pet_delete(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).get()
#
#     form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         form.save()
#         return redirect("index")
#
#     context = {
#         "form": form,
#         "username": username,
#         "pet": pet,
#     }
#     return render(
#         request,
#         "pets/delete_pet.html",
#         context
#     )
