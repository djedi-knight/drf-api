from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from books import views


urlpatterns = {
    url(r'^$', views.index_view, name="index_view"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
