from django.db import models

# Create your models here.
class Scout(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=40)
    age = models.BooleanField()
    dob = models.DateField()
    contact = models.TextField(max_length=13)
    s_contact = models.TextField(max_length=13)
    country = models.TextField(max_length=10)
    city = models.TextField(max_length=10)
    reffral = models.TextField()
    experienced = models.BooleanField()
    work_status = models.BooleanField()
    associated_clubs = models.TextField()
    course = models.BooleanField()

    def __str__(self):
        return (self.email)
