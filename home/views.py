from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.utils.html import strip_tags
from .models import Post, Comment
from .forms import ArticleForm, CommentForm
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    conatcts = Post.objects.all().order_by('-last_updated')
    length = len(conatcts)
    paginator = Paginator(conatcts, 8)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "home\index.html", {"contacts": posts, 'page': page, 'length': length})

@login_required(login_url='/members/login')
def Article(request):
    submitted = False
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = request.POST.get('f_name',)
            email = request.POST.get('email',)
            title = request.POST.get('title',)
            sdesc = request.POST.get('sdesc',)
            content = cd['article']
            author = request.user
            striped_content = strip_tags(cd['article'])
            if 'img' in request.FILES:
                img = request.FILES['img']
                # print(img)
                p = Post(name=name, title=title, shortdescription=sdesc, email=email,
                         desc=content, image=img, striped_desc=striped_content, author=author)
                p.save()
            else:
                p = Post(name=name, title=title, shortdescription=sdesc,
                         email=email, desc=content, striped_desc=striped_content, author=author)
                p.save()
            return redirect('/article?submitted=True')
    else:
        form = ArticleForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/article.html', {'form': form, 'submitted': submitted})


def detail(request, name, id):
    post = get_object_or_404(Post, pk=id, name=name)
    comments = post.comments.filter(active=True).order_by('-updated')
    new_comment = None
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments,
               'new_comment': new_comment, 'comment_form': comment_form,'total_likes':post.total_likes,'liked':liked}
    return render(request, 'home/detail.html', context)
    # return render(request, 'home/lat_detail.html', context)


def pdf(request, id):
    post = get_object_or_404(Post, pk=id)
    path = post.file
    # print(path)
    # return HttpResponse(f"This is id {id}")
    pdf_data = open(
        r"D:\Academics\IIMUN Internship\Website\substance-root\media\pdf\test.pdf", "rb").read()
    return HttpResponse(pdf_data, content_type="application/pdf")


class update(LoginRequiredMixin,UpdateView):
    login_url = '/members/login'
    model = Post
    fields = ('title', 'shortdescription', 'image', 'desc')
    template_name = 'home/update.html'


class delete_post(LoginRequiredMixin,DeleteView):
    login_url = '/members/login'
    model = Post
    template_name = 'home/delete.html'
    success_url = reverse_lazy('index')


class update_comments(LoginRequiredMixin,UpdateView):
    login_url = '/members/login'
    model = Comment
    template_name = 'home/update_comment.html'
    form_class = CommentForm
    # fields = ('name','email','body')
    # def get_form(self, form_class=CommentForm):
    #     form = super().get_form(form_class=form_class)
    #     form.fields["body"].label = "Comment"

    # success_url = '/'
    # def get_object(self, queryset=None):
    #     self.pk = self.kwargs.get('pk', None)
    #     posts = Comment.objects.get(pk=self.pk).post
    #     print(posts.id)
    #     success_url =  reverse_lazy('detail', args=[str(posts.name), str(posts.id)])
    # success_url = reverse('detail', args=[str(posts.name), str(posts.id)])


class delete_comment(LoginRequiredMixin,DeleteView):
    login_url = '/members/login'
    model = Comment
    template_name = 'home/delete_comment.html'
    # success_url = reverse_lazy('index')

    def get_success_url(self):
        pk = self.kwargs["pk"]
        post = Comment.objects.get(pk=pk).post
        # return reverse("detail", kwargs={"name":post.name,"id": post.id})
        return reverse('home:detail',args=[str(post.name),str(post.id)])

def LikeView(request,name,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('home:detail', args=[str(name),str(pk)]))
