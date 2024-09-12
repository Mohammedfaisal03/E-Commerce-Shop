from django.db import models

# Create your models here.

class Contact(models.Model):
    user_first_name=models.CharField(max_length=200)
    user_last_name=models.CharField(max_length=200,null=True,blank=True)
    user_email=models.EmailField(max_length=254)
    user_message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user_first_name