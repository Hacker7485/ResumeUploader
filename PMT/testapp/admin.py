from django.contrib import admin
from testapp.models import Client,Project+
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display=['client_name','created_at','created_by']

admin.site.register(Client,ClientAdmin)
admin.site.register(Project)
