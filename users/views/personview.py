from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms import PersonRegisterForm, UserUpdateForm, PersonUpdateForm
from django.apps import apps
from ..models import Person


# Create your views here.
def register_person(request):
    if request.method == 'POST':
        form = PersonRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Din Person-bruker har blitt opprettet! Du kan nå logge inn.  ')
            return redirect('news-home')
        else:
            messages.warning(request, 'Registrering ikke vellykket. Prøv igjen.  ')
    else:
        form = PersonRegisterForm()
    return render(request, 'person/register_person.html', {'form': form})


# Allows you to have access to your profile if logged in.
@login_required
def profile(request):

    return render(request, 'person/profile.html')


# Allows you to have access to your profile if logged in
# Gets forms from to edit info to the edit view
@login_required
def edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PersonUpdateForm(request.POST,
                                  request.FILES,
                                  instance=request.user.person_profile)



        if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()

           messages.success(request, 'Din profil har blitt endret')
           return redirect('/person/profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PersonUpdateForm(instance=request.user.person_profile)


    context = {
        'u_form': u_form,
        'p_form': p_form


    }
    return render(request, 'person/edit.html', context)


def browse(request):
    return render(request, 'person/browse.html')