from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField()
    technologies = models.CharField(max_length=350)
    live_link = models.URLField(blank=True, null=True)
    github_lin = models.URLField(blank=True, null=True)
    image = models.ImageField( upload_to="projects/")


    def __str__(self):
        return self.title
    


class Blog(models.Model):
     title = models.CharField(max_length=200)
     content = models.TextField()
     published_date = models.DateTimeField(auto_now_add=True)
     tags = models.CharField(max_length=300)
     thumbnail = models.ImageField(upload_to="blog/")
 
     def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name