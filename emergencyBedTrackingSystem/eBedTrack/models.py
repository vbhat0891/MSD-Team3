from django.db import models
from django.utils import timezone

class patient(models.Model):
    patientId =  models.AutoField(primary_key=True)
    firstName = models.CharField("Patient's first name", max_length=100 ,default='Patients first name')
    lastName = models.CharField("Patient's last name",max_length=100,default='Patients last name')
    sex = models.CharField("Patient's sex",max_length=20,default='Male/Female/Other')
    pTimeOfAdmission = models.DateTimeField(default=timezone.now)
    pCondition = models.CharField(max_length= 50,default='Patients initial condition')
    pBedType = models.CharField(max_length= 50)
    pModeOfArrival = models.CharField(max_length=50)
    pAge = models.IntegerField()
    pBirthDate = models.DateTimeField(default=timezone.now)
    pPhoneNo = models.CharField(max_length=12)
    injuries =models.CharField(max_length= 50)
    deposition = models.CharField(max_length=50)
    pTimeOfSurgery = models.DateTimeField (default=timezone.now)
    kinName = models.CharField(max_length=150)
    relation = models.CharField(max_length=50)
    pTimeOfDeath = models.DateTimeField(default=timezone.now)
    nurseId = models.ForeignKey(nurse, on_delete=models.CASCADE)
    bedId = models.ForeignKey(bedInfo, on_delete=models.CASCADE)

    def created(self):
        self.pTimeOfAdmission = timezone.now()
        self.save()

    def updated(self):
        self.pTimeOfAdmission = timezone.now()
        self.save()

    def __str__(self):
        return self.patientId

class nurse(models.Model):
    nurseId = models.AutoField(primary_key=True)
    nFirstName = models.CharField("Nurse's first name",max_length=100,default='Nurse first name')
    nLastName = models.CharField("Nurse's first name",max_length=100,default='Nurse last name')
    nAddress = models.CharField(max_length=250)
    nPhoneNo = models.CharField(max_length=12)
    hospitalId = models.ForeignKey(hospital, on_delete=models.CASCADE)
    adminId = models.ForeignKey(administrator, on_delete=models.CASCADE)

    def __str__(self):
        return self.nurseId

class bedInfo(models.Model):
    bedId = models.AutoField(primary_key=True)
    bedType = models.CharField(max_length=50)
    #hospitalId = models.ForeignKey(hospital, on_delete=models.CASCADE)


    def __str__(self):
        return self.bedId

class hospital(models.Model):
    hospitalId = models.AutoField(primary_key=True)
    hospitalName = models.CharField(max_length=100)
    hospitalAddress = models.CharField(max_length=250)
    hospitalPhoneNo = models.CharField(max_length=12)
    adminId = models.ForeignKey(administrator, on_delete=models.CASCADE)

    def __str__(self):
        return self.hospitalId

class administrator(models.Model):
    adminId = models.AutoField(primary_key=True)
    adminName = models.CharField(max_length= 100)

    def __str__(self):
        return self.adminId


class nurseBed(models.Model):
    nurseBedId = models.AutoField(primary_key=True)
    nurseId = models.ForeignKey(nurse, related_name='nurseId')
    bedId = models.ForeignKey(bedInfo, related_name='bedId')


    def __str__(self):
        return self.nurseBedId
