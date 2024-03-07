from django.urls import path, include
from petstagram.accounts import views

urlpatterns = (
    path('register/', views.SignUpUserView.as_view(), name='signup user'),
    path('login/', views.SignInUserView.as_view(), name='signin user'),
    path('logout/', views.signout_user, name='signout user'),

    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailsView.as_view(), name='details profile'),
        path('edit/', views.EditProfileView.as_view(), name='edit profile'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete profile'),
    ])),
)
