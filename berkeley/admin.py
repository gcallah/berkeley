from django.contrib import admin

# Register your models here.
from .models import Person
from .models import Publisher
from .models import Publication

admin.site.register(Person)
admin.site.register(Publisher)
admin.site.register(Publication)
