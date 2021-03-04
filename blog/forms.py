from django import forms
from .models import Post, Category, Comment

#para generar el dropdown de las categorías

"""def choice_list():
	choices = Category.objects.all().values_list('name','name')

	choice_list = []
	for item in choices:
		choice_list.append(item)
	
	return choice_list"""


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'category', 'body', 'header_image')
		category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.SelectMultiple, required=False)

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert title'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
			#'category': forms.Select(queryset=Category.objects.all(), attrs={'class': 'form-select'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insert text'}),

		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
			'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insert text', 'rows':'5'}),

		}

