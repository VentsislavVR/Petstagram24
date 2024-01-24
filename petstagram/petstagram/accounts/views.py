from django.shortcuts import render, redirect


# Create your views here.
def profile_register(request):
    context = {}
    return render(
        request,
        'accounts/register-page.html',
        context
    )


def profile_login(request):
    context = {}

    return render(
        request,
        'accounts/login-page.html',
        context
    )


def profile_logout(request):
    return redirect('index')


def profile_details(request, pk):

    context = {}
    return render(
        request,
        'accounts/profile-details-page.html',
        context
    )


def profile_edit(request, pk):
    context = {}

    return render(
        request,
        'accounts/profile-edit-page.html',
        context
    )


def profile_delete(request, pk):
    context = {}
    return render(
        request,
        'accounts/profile-delete-page.html',
        context
    )
