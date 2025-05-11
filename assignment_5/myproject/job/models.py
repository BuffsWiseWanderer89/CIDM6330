from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profilepic = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.username

class PhotoModel(models.Model):
    photo_id = models.AutoField(primary_key=True)
    image_url = models.URLField()
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return f"Photo {self.photo_id} by {self.user.username}"