from django.urls import path
from petstagram.common.views import IndexView, photo_like, photo_share, add_comment
urlpatterns = (
    path('',IndexView.as_view(),name='index'),
    path('pet_photo_like/<int:photo_id>/',photo_like,name='like'),
    path('share/<int:photo_id>/',photo_share,name='share'),
    path('comment/<int:photo_id>/',add_comment,name='comment'),
)