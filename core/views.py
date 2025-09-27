from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Announcement 
# Create your views here.

def base(request):
    return render(request, 'base.html', {'title': 'Base'})

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def arnwin(request):
    return render(request, 'arnwin.html', {'title': 'Arnwin'})

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, "announcements/list.html", {"announcements": announcements})

def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, pk=id)
    return render(request, "announcements/detail.html", {"announcement": announcement})
