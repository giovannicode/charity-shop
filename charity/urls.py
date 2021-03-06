from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'charity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^products/', include('products.urls', namespace='products'))
    url(r'^$', include('main.urls', namespace='main')),
    url(r'^admin/', include(admin.site.urls)),
)
