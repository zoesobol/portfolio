from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
class BlogView(ListView):
    model = models.Post
    template_name = 'blog.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = models.Category.objects.all()
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class PostDetailView(DetailView):
	model = models.Post
	initial = {'key': 'value'}
	template_name = 'post_details.html'
	form_class = forms.CommentForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comments'] = models.Comment.objects.filter(body=self.object)
		context['form'] = forms.CommentForm()
		return context
    
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# <process form cleaned data>
			new_comment = form.save(commit=False)
			new_comment.post = self.get_object()
			new_comment = form.save()
			return HttpResponseRedirect(self.request.path_info)

		return render(request, self.template_name, {'form': form})



"""
class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post_details.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = models.Comment.objects.filter(
            post=self.get_object()).order_by('-comment_date')
        data['comments'] = comments_connected
        data['comment_form'] = forms.CommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = models.Comment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)"""