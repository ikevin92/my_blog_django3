from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from posts.views import HelloWorld
# from posts.api.views import PostApiView, PostViewSet
from posts.api.router import router_post

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('posts/', HelloWorld.as_view())
    # path('api/posts/', PostApiView.as_view())
    path('api/', include(router_post.urls))
]
