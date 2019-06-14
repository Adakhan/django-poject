from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from main.forms import EditProfileForm

def about(request):
    return render(request, 'account/about.html')


def contact(request):
    return render(request, 'account/contact.html')


def profile(request):
    args = {'user': request.user}
    return render(request, 'account/profile.html', args)


def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'account/profile.html')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)


def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'account/profile.html')
        else:
            return render(request, 'account/change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'account/change_password.html', args)

