from django.urls import path
from . import views
from .views import update,delete_post,update_comments,delete_comment, LikeView
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('article',views.Article,name='article'),
    path('blog/<slug:pk>/delete', delete_post.as_view(), name='delete'),
    path('blog/<slug:pk>/comments/delete', delete_comment.as_view(), name='delete_comment'),
    # path('<int:id>',views.pdf,name='pdf'),
    path('blog/update/<int:pk>',update.as_view(),name='update'),
    path('blog/update/comment/<int:pk>',update_comments.as_view(),name='update_comment'),
    path('blog/<str:name>/<int:id>', views.detail, name='detail'),
    path('blog/<str:name>/<slug:pk>/like', LikeView, name='like_post'),
  

    
]