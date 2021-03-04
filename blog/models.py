from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#PARA VOLVER AL POST RECIEN CREADO
		#return reverse('post-detail', args=(str(self.id)))
		#PARA VOLVER A HOME
		return reverse('home')


class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	post_date = models.DateField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#PARA VOLVER A HOME
		return reverse('blog')

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	body = models.TextField()
	comment_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.post.title + ' | ' + self.name
	
	@property
	def number_of_comments(self):
		return BlogComment.objects.filter(blogpost_connected=self).count()
