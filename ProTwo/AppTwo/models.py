from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length = 264)
#     second_name = models.CharField(max_length = 264)
#     email = models.CharField(max_length = 264)
#
#     def __str__(self):
#         return (self.first_name + self.second_name)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete = AttributeError)

    profolio = models.URLField(blank = True)
    picture = models.ImageField(upload_to = 'profile_pics',blank = True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
