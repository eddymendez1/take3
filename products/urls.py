from django.conf.urls import url


from . import views
from .views import ProductListView, ProductDetailSlugView, add_comment_to_post


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^products/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]

