from django.db import models


class Blog_Post(models.Model):
    title = models.CharField(max_length=140)
    blog_code = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)
