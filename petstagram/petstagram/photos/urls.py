from django.urls import path, include
from petstagram.photos import views
from petstagram.photos.views import PetPhotoCreateView, PetPhotoDetailsView, PetPhotoEditView

urlpatterns = (
    path('create/', PetPhotoCreateView.as_view(), name='photo add'),
    path('<int:pk>/', include([
        path('', PetPhotoDetailsView.as_view(), name='details photo'),
        path('edit/', PetPhotoEditView.as_view(), name='edit photo'),
        path('delete/', views.delete_photo, name='delete photo'),
    ]))
)
