from django.contrib import admin
from testapp.models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','CV']


# Register your models here.
admin.site.register(Resume,ResumeAdmin)
