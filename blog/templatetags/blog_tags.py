from django import template
from ..models import Post, Category
 
register = template.Library()
 
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-id')[:num]

 
@register.simple_tag
def get_categories():
         # Don't forget to introduce the Category class at the top
    return Category.objects.all()