"""BudjetProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from budjetapp import views
from BudjetProject import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('login_signup/',views.login_signup,name='login_signup'),
    path('signup/',views.signup,name='signup'),
    path('experts/',views.experts,name='experts'),
    path('user_dashboard/',views.user_dashboard,name='user_dashboard'),
    path('my_slots/',views.my_slots,name='my_slots'),
    path('book_slot/<int:pk>',views.book_slot,name='book_slot'),

#path('graph/', views.Graph.as_view(), name='graph'),
path('graphs/',views.graphs,name='graph'),
    path('about/',views.about,name='about'),
    path('conults/',views.conults,name='conults'),
    path('cancel_slot/<int:pk>',views.cancel_slot,name='cancel_slot'),
    path('logout/',views.logouttt,name='logout'),
    path('expert_consultants/',views.expert_consultants,name='expert_consultants'),
    path('cons_expert/',views.cons_expert,name='cons_expert')
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
