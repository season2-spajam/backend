from django.db import models


class Post(models.Model):
    handle_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="images/")
    good_count = models.IntegerField(blank=True, default=0)
    caption = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        created_at_str = self.created_at.strftime("%Y/%m/%d %H:%M:%S")
        return f"({self.id}) {self.handle_name} : {created_at_str}"


class SingleImage(models.Model):
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"({self.id}) {self.img.name}"