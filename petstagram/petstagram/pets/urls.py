from django.urls import path, include

from petstagram.pets import views
from petstagram.pets.views import PetCreateView, PetDetailsView, PetEditView, PetDeleteView

urlpatterns = (
    path("add/", PetCreateView.as_view(), name="create pet"),
    path("<str:username>/pet/<slug:pet_slug>/",
         include([
             path("", PetDetailsView.as_view(), name="details pet"),
             path("edit/", PetEditView.as_view(), name="edit pet"),
             path("delete/", PetDeleteView.as_view(), name="delete pet"),
         ]))
)
