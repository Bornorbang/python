from django.contrib import admin
from django.http import HttpRequest
from app.models import GeneralInfo, Service, Testimony, Faq, ContactFormLog, Blog, Author

# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin (admin.ModelAdmin):
   pass

@admin.register(Service)
class ServiceAdmin (admin.ModelAdmin):
   list_display = [
      "title",
      "description"
   ]

   search_fields = [
      "title",
      "description"
   ]

@admin.register(Testimony)
class TestimonyAdmin (admin.ModelAdmin):
   list_display = [
      "username",
      "job",
      "rating_star",
      "review"
   ]

   def rating_star (self, obj):
      return '*' * obj.rating
   
   rating_star.short_description = "rating"

@admin.register(Faq)
class FaqAdmin (admin.ModelAdmin):
   list_display = [
      "faq_title",
      "faq_answer"
   ]
   
@admin.register(ContactFormLog)
class ContactFormLogAdmin (admin.ModelAdmin):

   list_display = [
      'email',
      'is_success',
      'is_error',
      'action_time'
   ]

   def has_add_permission(self, request, obj=None):
      return False
   
   def has_change_permission(self, request, obj=None):
      return False
   
   def has_delete_permission(self, request, obj=None):
      return False
   

@admin.register(Blog)
class BlogAdmin (admin.ModelAdmin):
   
   list_display = [
      'blog_title',
      'blog_author',
      'blog_image',
      'blog_category',
      'created_at',
   ]

@admin.register(Author)
class AuthorAdmin (admin.ModelAdmin):
   list_display = [
      'author_first_name',
      'author_last_name',
      'joined_at'
   ]