from django.views.generic import edit, DetailView, ListView
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.urls import reverse
from django.http import HttpResponse


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.order_by('-published_at')[:5]


class PostDetailView(edit.FormMixin, DetailView):
    model = Post
    pk_url_kwarg = "id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    template_name = 'detail.html'
    form_class = CommentForm
    
    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object, 'author': self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post = self.object
        obj.user = self.request.user
        # saving the test
        obj.save()
        form.save()
        return super(PostDetailView, self).form_valid(form)

