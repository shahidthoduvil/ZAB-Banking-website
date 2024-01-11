from django.db import models
from django.contrib.auth.models import User

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class CustomrerApplication(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Saving Account'),
        ('current', 'Current Account'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    material_provide = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return self.user.username
