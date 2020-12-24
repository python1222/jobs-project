from django.contrib import admin
from .models import Hyd_jobs,Pune_jobs,Bang_jobs

# Register your models here.
class Hyd_jobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','email','phonenumber']
class Bang_jobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','email','phonenumber']
class Pune_jobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','email','phonenumber']
admin.site.register(Hyd_jobs,Hyd_jobsAdmin)
admin.site.register(Bang_jobs,Bang_jobsAdmin)
admin.site.register(Pune_jobs,Pune_jobsAdmin)