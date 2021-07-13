from django.db import models

# Create your models here.

STATE_CHOICE = (
('Lucknow','Lucknow'),
('Mumbai','Mumbai'),
('Thane','Thane'),
('Kalyan','Kalyan'),
('Borivali','Borivali'),
)


class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile',blank=True)
    CV=models.FileField(upload_to='resume',blank=True)
