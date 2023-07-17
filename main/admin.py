from django.contrib import admin
from .models import CleaningService, Booking

# Register the models with the admin site using the default UserAdmin class
admin.site.register(CleaningService)
admin.site.register(Booking)



