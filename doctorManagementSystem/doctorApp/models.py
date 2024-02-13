from django.db import models

class Speciality(models.Model):
    specialist = models.CharField(max_length=255)

    def __str__(self):
        return self.specialist

class Location(models.Model):
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    fees = models.IntegerField()
    experience = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} - {self.speciality} - {self.location} - Exp-{self.experience} Years'
    
