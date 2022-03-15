from django.views import generic
from django.urls import reverse_lazy

from .models import PostBlog
from.form import AddNewPost


class PostList(generic.ListView):
    model = PostBlog
    template_name = 'blog/post_list.html'
    context_object_name = 'posts_list'


class PostIdDetail(generic.DetailView):
    model = PostBlog
    template_name = 'blog/postdetail.html'
    context_object_name = 'post'


class AddPost(generic.CreateView):
    form_class = AddNewPost
    template_name = 'blog/post_creat.html'


class EditPost(generic.UpdateView):
    model = PostBlog
    form_class = AddNewPost
    template_name = 'blog/post_creat.html'


class PostDelete(generic.DeleteView):
    model = PostBlog
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
#
# def post_delete(request, pk):
#     post = get_object_or_404(PostBlog, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})
#















