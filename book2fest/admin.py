from django.contrib import admin
from book2fest.models import Artist, OrganizerProfile, UserProfile, Genre, Category

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(OrganizerProfile)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Category)