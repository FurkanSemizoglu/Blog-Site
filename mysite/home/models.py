from django.db import models

# Create your models here.


class Blog(models.Model):
    title  = models.CharField(("Blog Başlık"),max_length=50)
    description = models.TextField(("açıklama") , max_length=500)
    image = models.ImageField(upload_to="./template/static/iamges")
    datetime = models.DateTimeField(("tarih"),auto_now_add=True)


    def __str__(self):
        return self.title
    

