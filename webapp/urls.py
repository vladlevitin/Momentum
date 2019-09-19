"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import startupsview, investorview, personview, jobview
from users.views.jobview import JobDetailView, JobCreateView, JobUpdateView, JobDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),                                                                # Admin http://127.0.0.1:8000/admin/
    path('', include('news.urls')),                                                                 # Homepage http://127.0.0.1:8000/
    path('register_startup/', startupsview.register_startup, name='register_startup'),              # Register http://127.0.0.1:8000/register_startup/
    path('startups/profile/', startupsview.profile, name='startup_profile'),                        # Profil http://127.0.0.1:8000/startups/profile/
    path('register_investor/', investorview.register_investor, name='register_investor'),           # Register http://127.0.0.1:8000/register_investor/
    path('investor/profile/', investorview.profile, name='investor_profile'),                       # Profil http://127.0.0.1:8000/investor/profile/
    path('register_person/', personview.register_person, name='register_person'),                   # Register http://127.0.0.1:8000/register_person/
    path('person/profile/', personview.profile, name='person_profile'),                             # Profil http://127.0.0.1:8000/person/profile/
    path('login/', auth_views.LoginView.as_view(template_name='news/login.html'), name='login'),    # Login http://127.0.0.1:8000/
    path('logout/', auth_views.LogoutView.as_view(template_name='news/base.html'), name='logout'),  # Logout http://127.0.0.1:8000/

    path('startups/<int:pk>', startupsview.visit, name='visit_startup'),
    path('startups/browse/', startupsview.browse, name='browse_startup'),                           # All Startups at http://127.0.0.1:8000/startups/browse/

    path('investors/<int:pk>', investorview.visit, name='visit_investor'),
    path('investors/browse/', investorview.browse, name='browse_investor'),                         # All Investors at http://127.0.0.1:8000/investor/browse/
    path('person/browse/', personview.browse, name='browse_person'),                                # All Persons at http://127.0.0.1:8000/person/browse/
    path('jobs/browse/', jobview.browse, name='browse_jobs'),                                       #All jobs at http://127.0.0.1:8000/jobs/browse/
    path('jobs/browse/job/<int:pk>', JobDetailView.as_view(), name='job_detail'),                   #Specific job at http://127.0.0.1:8000/jobs/browse/job/<int:pk>
    path('jobs/new/', JobCreateView.as_view(template_name='jobs/job_form.html'), name='job_create'),                                    #Create a new job at http://127.0.0.1:8000/jobs/new/
    path('jobs/browse/job/<int:pk>/update', JobUpdateView.as_view(template_name='jobs/job_form.html'), name='job_update'),              #Update a specific job at http://127.0.0.1:8000/jobs/browse/job/<int:pk>/update
    path('jobs/browse/job/<int:pk>/delete', JobDeleteView.as_view(template_name='jobs/job_confirm_deletes.html'), name='job_delete'),   #Delete a specific job at http://127.0.0.1:8000/jobs/browse/job/<int:pk>/delete

    path('person/profile/edit', personview.edit, name='edit_person'),                               # Edit profile http://127.0.0.1:8000/profile/edit
    path('startups/profile/edit', startupsview.edit, name='edit_startup'),                          # Edit profile http://127.0.0.1:8000/profile/edit
    path('investor/profile/edit', investorview.edit, name='edit_investor'),                         # Edit profile http://127.0.0.1:8000/profile/edit


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




