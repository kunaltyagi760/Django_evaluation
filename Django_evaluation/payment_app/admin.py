from django.contrib import admin
from .models import Service, ServiceUser, Subscription

class UserAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_filter = ['gender']

admin.site.register(ServiceUser, UserAdmin)
admin.site.register(Subscription)
admin.site.register(Service)



# Register your models here.
