from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm, EditProfileForm
from django.urls import reverse_lazy


# Create your views here.
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home:index')


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home:index')

    def get_object(self):
        return self.request.user