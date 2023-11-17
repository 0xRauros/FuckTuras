from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile, Settings
from invoices.models import Invoice
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create new user object but avoid saving it
            new_user = user_form.save(commit=False)
            # set the chosen password
            # password hassing method (set_password())
            new_user.set_password(
                user_form.cleaned_data['password'])
            # save the user object
            new_user.save()
            # create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    '''Account edit (User & Profile models)'''
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST) # isntance gets the existing date from the current user so we can edit.
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def dashboard(request):
    invoices = Invoice.objects.filter(user=request.user.id)[:3]
    return render(request, 'account/dashboard.html',
                  {'section': 'dashboard',
                   'invoices': invoices})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile

    fields = ('photo', 
              'address', 
              'city', 
              'description', 
              'phone', 
              'email',
              'website')
    
    success_url = '/'
    template_name = 'account/profile/profile_form.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'account/profile/profile_detail.html'



class SettingsDetailView(LoginRequiredMixin, DetailView):
    '''
        Platform current settings.
        - Colors
    '''
    model = Profile
    template_name = 'account/settings/settings_detail.html'

