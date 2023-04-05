from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='authors/',null=True,blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,blank=True)
    sort = models.TextField(max_length=130)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')
    pdf_file = models.FileField(upload_to='bookspdf/')

    def __str__(self):
        return self.title
