# Inside your app's models.py (e.g., gallery/models.py)

from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    # Add other fields if necessary, like user or description
