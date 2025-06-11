from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(users)
admin.site.register(movie_info)
admin.site.register(seat_info)
admin.site.register(theatre_info)
admin.site.register(show_info)
