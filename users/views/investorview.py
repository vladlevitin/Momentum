from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms import InvestorRegisterForm, UserUpdateForm, InvestorUpdateForm
from django.apps import apps


Investor = apps.get_model('users', 'Investor')
Status_interest = apps.get_model('users', 'Status_interest')
Industry = apps.get_model('users', 'Industry')
Sector = apps.get_model('users', 'Sector')
Status = apps.get_model('users', 'Status')


# Create your views here.
def register_investor(request):
    if request.method == 'POST':
        form = InvestorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Din Investor-bruker har blitt opprettet! Du kan nå logge inn.  ')
            return redirect('news-home')
        else:
            messages.warning(request, 'Registrering ikke vellykket. Prøv igjen.  ')
    else:
        form = InvestorRegisterForm()
    return render(request, 'investor/register_investor.html', {'form': form})


# Requires login for access
@login_required
def profile(request):
    return render(request, 'investor/profile.html')


# Requires login for access to profile.
# Fetches forms for editing within edit.
@login_required
def edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = InvestorUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.investor_profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Din profil har blitt endret')
            return redirect('/investor/profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = InvestorUpdateForm(instance=request.user.investor_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'investor/edit.html', context)


def browse(request):
    context = {
        'all_investor': Investor.objects.all(),
        'all_status': Status_interest.objects.all()
    }
    return render(request, 'investor/browse.html', context)

def visit(request, pk):
    context = {
        'investor': Investor.objects.get(pk=pk)
    }
    return render(request, 'investor/visit.html', context)