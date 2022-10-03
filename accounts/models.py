from django.db import models
from django_countries.fields import CountryField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


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
    city = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.username


    class Meta:
        ordering = ["id"]
