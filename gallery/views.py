# Inside your app's views.py (e.g., gallery/views.py)

from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

def photo_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'gallery/photo_upload.html', {'form': form})

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/gallery.html', {'photos': photos})
