from django.contrib import admin
from dogs.models import Dog


class DogsAdmin(admin.ModelAdmin):
    fields = ['name', 'owner', 'photo']

admin.site.register(Dog, DogsAdmin)
