from django.contrib import admin
from .models import Hotel, Review
# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('hotel_name',)}
    
admin.site.register(Hotel, HotelAdmin)

admin.site.register(Review)