from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(max_length=30)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts', default=1)
    title = models.CharField(default="My article", max_length=100)
    shortdescription = models.CharField(
        default="This is a shor description of my Article", max_length=100)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField()
    file = models.FileField(default='pdf/test.pdf', upload_to='pdf/')
    image = models.ImageField(
        default='img/slider2.jpg', upload_to='article_cover/')
    desc = RichTextField()
    likes = models.ManyToManyField(User,related_name='blog_post')
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10, default='draft')
    striped_desc = RichTextField(default="", editable=False)
    date_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('home:detail', args=[str(self.name), str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def get_absolute_url(self):
        post = Comment.objects.get(pk=self.pk).post  # new
        print(post.id)
        return reverse('home:detail', args=[str(post.name), str(post.id)])

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
