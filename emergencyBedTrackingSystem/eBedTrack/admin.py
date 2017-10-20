from django.contrib import admin
from .models import patient,hospital, bedInfo, nurseBed, administrator, nurse

# Register your models here.
class PatientList(admin.ModelAdmin):
    list_display = ('patientId','firstName','lastName','sex' )
    list_filter = ('patientId','firstName','lastName','sex' )
    search_fields =('firstName','lastName')
    ordering = ['firstName']


class HospitalList(admin.ModelAdmin):
    list_display = ('hospitalId', 'hospitalName', 'hospitalAddress', 'hospitalPhoneNo')
    list_filter = ('hospitalId', 'hospitalName', 'hospitalAddress', 'hospitalPhoneNo')
    search_fields = ('hospitalName', 'hospitalAddress', 'hospitalPhoneNo')
    ordering = ['hospitalName']


class NurseList(admin.ModelAdmin):
    list_display = ('nurseId', 'nFirstName', 'nLastName', 'hospitalId')
    list_filter = ('nurseId', 'nFirstName', 'nLastName', 'hospitalId')
    search_fields = ( 'nFirstName', 'nLastName', 'hospitalId')
    ordering = ['nFirstName']

class bedInfoList(admin.ModelAdmin):
    list_display = ('bedId', 'bedType', 'hospitalId')
    list_filter = ('bedId', 'bedType',  'hospitalId')
    search_fields = ('bedId', 'bedType',  'hospitalId')
    ordering = ['bedType']

class administratorList(admin.ModelAdmin):
    list_display = ('adminId', 'adminName')
    list_filter = ('adminId', 'adminName')
    search_fields = ('adminId', 'adminName')
    ordering = ['adminName']

class nurseBedList(admin.ModelAdmin):
   list_display = ('nurseBedId', 'nurseId', 'bedId')
   list_filter = ('nurseBedId', 'nurseId', 'bedId')
   search_fields = ('nurseBedId', 'nurseId', 'bedId')
   ordering = ['nurseBedId']

admin.site.register(patient, PatientList)
admin.site.register(hospital, HospitalList)
admin.site.register(nurse, NurseList)
admin.site.register(bedInfo, bedInfoList)
admin.site.register(administrator, administratorList)
admin.site.register(nurseBed, nurseBedList)

