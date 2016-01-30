from django.shortcuts import render
from portfolioapp.models import Blog_Post
from django.views.generic import CreateView, DetailView, ListView
from rest_framework import generics
from rest_framework import serializers
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from portfolioapp.forms import UserForm
from django.shortcuts import render_to_response, redirect

# def blog_template(request):
#     print("test")
#     return render(request, template_name="blogpost.html")

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('login')
        else:
            pass
    else:
        user_form = UserForm()
    return render_to_response(
        'register.html',
        {'user_form': user_form, 'registered': registered},
        context)


class PBlog(DetailView):
    queryset = Blog_Post.objects.all()


class PBlog_Create(CreateView):
    model = Blog_Post
    fields = ['title', 'blog_code']

    def get_success_url(self):
        return reverse_lazy('blog_post', args=(self.object.id,))


class PBlog_List(ListView):
    queryset = Blog_Post.objects.all()

# API Views
#######################


# class PostSerializer(serializers.ModelSerializer):
#         model = Blog_Post
#
#         class Meta:
#             model = Blog_Post


# class PBlog(generics.RetrieveAPIView):
#     queryset = Blog_Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PBlog_Create(generics.ListCreateAPIView):
#     model = Blog_Post
#     serializer_class = PostSerializer
