from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default="Web Designer Nigeria")
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(max_length=100, blank=True, null=True)
    twitter_url = models.URLField(max_length=100, blank=True, null=True)
    facebook_url = models.URLField(max_length=100, blank=True, null=True)
    instagram_url = models.URLField(max_length=100, blank=True, null=True)
    linkedin_url = models.URLField(max_length=100, blank=True, null=True)


    def __str__(self):
      return self.company_name

class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()

    def __str__(self):
       return self.title
class Testimony(models.Model):
   image = models.CharField(max_length=255, null= True, blank = True)
   stars_count = [
      (1, 'one'),
      (2, "two"),
      (3, "three"),
      (4, "four"),
      (5, "five")
   ]
   rating = models.IntegerField(choices=stars_count)
   username = models.CharField(max_length=255)
   job = models.CharField(max_length=255)
   review = models.TextField()

   def __str__(self):
      return self.username

class Faq(models.Model):
   faq_title = models.CharField(max_length=255)
   faq_answer = models.TextField()

class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank = True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(null=True,blank=True)

    def __str__(self):
      return self.email
    

class Author(models.Model):
   author_first_name = models.CharField(max_length=50)
   author_last_name = models.CharField(max_length=50)
   author_image = models.CharField(max_length=255, null=True, blank=True)
   author_country = models.CharField(max_length=50 )
   joined_at = models.DateTimeField(null=True, blank=True)

   def __str__(self):
      return f"{self.author_first_name} {self.author_last_name}"


class Blog(models.Model):
    blog_image = models.CharField(max_length=255, blank=True, null=True)
    blog_category = models.CharField(max_length=50)
    blog_title = models.CharField(max_length=100)
    blog_author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    blog_content =  RichTextField()


    def __str__(self):
        return self.blog_title
