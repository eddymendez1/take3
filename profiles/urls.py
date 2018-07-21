from django.conf.urls import include, url


from .views import ProfileDetailSlugView, profile_page#, edit_profile
#EditProfile

urlpatterns = [
    #/profile/
    url(r'^$', profile_page, name='create'),

    #/profiles/<Slug>/
    url(r'^(?P<slug>[\w-]+)/$', ProfileDetailSlugView.as_view(), name='views'),

    #/profile/<Slug>/edit
    #url(r'^(?P<slug>[\w-]+)/edit/$', edit_profile, name='edit'),
]
