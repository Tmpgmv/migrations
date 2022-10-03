from django.db import models
from django.utils.deconstruct import deconstructible
from django_countries.fields import CountryField


@deconstructible
class UploadTo():

    def __init__(self, a_dir):
        self.a_dir = a_dir

    def __call__(self, instance, filename):
        return '{}/{}'.format(self.a_dir,
                               filename)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birth = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=36)
    about_human = models.TextField()
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=False)
    country = CountryField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to=UploadTo(a_dir="trololo"),
                            null=True,
                            blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["id"]
