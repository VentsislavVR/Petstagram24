from django.urls import path, include
from petstagram.accounts import views

urlpatterns = (
    path('register/', views.signup_user, name='signup user'),
    path('login/', views.signin_user, name='signin user'),
    path('logout/', views.signout_user, name='signout user'),

    path('profile/<int:pk>/', include([
        path('', views.details_profile, name='details profile'),
        path('edit/', views.edit_profile, name='edit profile'),
        path('delete/', views.delete_profile, name='delete profile'),
    ])),
)
