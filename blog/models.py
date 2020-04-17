from django.db import models


class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=50, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title
