from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
# Create your views here.
from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreateForm
from petstagram.accounts.models import Profile


# class OwnerRequiredMixin(AccessMixin):
#     """Verify that the current user is authenticated."""
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user != kwargs.get('pk',None):
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)
class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = PetstagramUserCreateForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)
        return result


LogoutUserView = auth_views.LogoutView


def signout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects \
        .select_related('user').all()
    template_name = 'accounts/details_profile.html'


class EditProfileView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    queryset = Profile.objects.select_related('user').all()

    template_name = 'accounts/edit_profile.html'

    fields = ('first_name', 'last_name',
              'picture', 'date_of_birth')

    def get_success_url(self):
        return reverse_lazy(
            'details profile',
            kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_of_birth'].widget.attrs['type'] = 'date'
        form.fields['date_of_birth'].label = 'Birthday'
        return form
    #Todo labels


class ProfileDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    queryset = Profile.objects.select_related('user').all()

    template_name = 'accounts/delete_profile.html'

    success_url = reverse_lazy('index')
