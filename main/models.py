from django.db import models

# Create your models here.



class Home(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class AboutUs(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body
    

class Reklamalar(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()


class Service(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.FileField(upload_to='service/')
    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
  

class Xabar_qoldirish(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
