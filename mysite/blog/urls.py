from django.conf.urls import url
from . import views

# http://www.tohuandkonsome.site/entry/2017/06/10/211145
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_details, name="post_details"),
]
