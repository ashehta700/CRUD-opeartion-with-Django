from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.  Tablesss

# class person (models.Model):
#     name = models.CharField(max_length=50)
    
# class group (models.Model):
#     name =models.CharField(max_length=50)
#     members= models.ManyToManyField(
#         person,
#         through='membership',
#         through_fields=('group','person')
#     )   

# class membership(models.Model):
#     group=models.ForeignKey(group,on_delete=models.CASCADE)     
#     person=models.ForeignKey(person,on_delete=models.CASCADE) 
#     invite_person=models.CharField(max_length=50)    
   
class Post(models.Model):
    author = models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title    
                