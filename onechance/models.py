from django.db import models

# Create your models here.

class Post(models.Model):
    handle_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    good_count = models.IntegerField(default=0)
    caption = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.handle_name + ": " + str(self.created_at)