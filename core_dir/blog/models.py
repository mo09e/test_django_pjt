from django.db import models


class Post(models.Model):    
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.body} {self.author}"

    class Meta:
        verbose_name_plural = "Posts"

class Author(models.Model):    
    name = models.CharField(max_length=255, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Authors"

