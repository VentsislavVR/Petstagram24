from django.urls import path
from petstagram.common import views
urlpatterns = (
    path('',views.index,name='index'),
    path('pet_photo_like/<int:photo_id>/',views.photo_like,name='like'),
    path('share/<int:photo_id>/',views.photo_share,name='share'),
)