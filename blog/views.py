from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic
from .forms import CommentForm

def get_comment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    return render(request, 'name.html', {'form': form})

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.order_by('-published_at')[:5]


class DetailView(generic.DetailView):
    model = Post
    pk_url_kwarg = "id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    template_name = 'detail.html'

