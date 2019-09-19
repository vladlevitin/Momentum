from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms import StartupRegisterForm, UserUpdateForm, StartupUpdateForm
from django.apps import apps
import googlemaps

Startup = apps.get_model('users', 'Startup')
Industry = apps.get_model('users', 'Industry')
Sector = apps.get_model('users', 'Sector')
Status = apps.get_model('users', 'Status')
Job = apps.get_model('users', 'Job')


# Create your views here.
def register_startup(request):
    if request.method == 'POST':
        form = StartupRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Din startup-bruker har blitt opprettet! Du kan nå logge inn.  ')
            return redirect('news-home')
        else:
            messages.warning(request, 'Registrering ikke vellykket. Prøv igjen.  ')
    else:
        form = StartupRegisterForm()
    return render(request, 'startups/register_startup.html', {'form': form})


# Requires login for access to profile.
@login_required
def profile(request):
    all_jobs = Job.objects.all()
    return render(request, 'startups/profile.html', {'all_jobs': all_jobs})


# Requires login for access to profile.
# Fetches form for editing in edit.
@login_required
def edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = StartupUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.startup_profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Din profil har blitt endret')
            return redirect('/startups/profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = StartupUpdateForm(instance=request.user.startup_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'startups/edit.html', context)


def browse(request):
    context = {
        'all_startups': Startup.objects.all(),
        'all_industry': Industry.objects.all(),
        'all_sectors': Sector.objects.all(),
        'all_status': Status.objects.all()
    }
    return render(request, 'startups/browse.html', context)


def visit(request, pk):
    context = {
        'startup': Startup.objects.get(pk=pk),
        'all_jobs': Job.objects.all()
    }
    return render(request, 'startups/visit.html', context)
