from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from books import views


urlpatterns = {
    url(r'^$', views.index_view, name="index_view"),
    url(r'^authors/$', views.AuthorView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>[\d]+)/$', views.AuthorInstanceView.as_view(), name='author-instance'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
