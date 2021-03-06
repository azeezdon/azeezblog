"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from post.views import PostListView,post_search,  post_detail, tagged,CategoryView, CategoryListView  #CategoryListView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from django.conf.urls import url
from .feeds import LatestPostsFeed

sitemaps = {
     "posts": PostSitemap,
}
urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', PostListView.as_view(), name='blog'),
    path('search/', post_search, name='post_search'),
    path('<slug:post>/', post_detail, name='post_detail'),
    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('tag/<slug:slug>/', tagged, name="tagged"),
    path('category/<slug:slug>/', CategoryView, name='category'),
    path('category-list/', CategoryListView.as_view(), name='category-list'),


    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
