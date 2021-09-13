from django.contrib import admin
from .models import Artist
from .models import Photo


admin.site.register(Artist)
admin.site.register(Photo)
