from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'TechWise.views.index',name='index'), #for Sangit
    url(r'^contact/$', 'TechWise.views.contact', name='contact'),#for signup
    url(r'^event/$', 'TechWise.views.event', name='event'), #for Nirbhay
    url(r'^reference/$', 'TechWise.views.reference', name='reference'), 
    url(r'^watson/$', 'TechWise.views.watson', name='watson'),
    url(r'^signup/$', 'TechWise.views.signup', name='signup'), 
    url(r'^selection/$', 'TechWise.views.selection', name='selection'), #for Mounika
    url(r'^statistics/$', 'TechWise.views.statistics', name='statistics'),
    url(r'^analytics/$', 'TechWise.analytics.main',name='analytics'),

    #Language Pages
    url(r'^reference/html/$', 'TechWise.views.html', name='html'),
    url(r'^reference/css/$', 'TechWise.views.css', name='css'),
    url(r'^reference/js/$', 'TechWise.views.js', name='js'),
    url(r'^reference/bootstrap/$', 'TechWise.views.bootstrap', name='bootstrap'),
    url(r'^reference/perl/$', 'TechWise.views.perl', name='perl'),
    url(r'^reference/php/$', 'TechWise.views.php', name='php'),
    url(r'^reference/nodejs/$', 'TechWise.views.nodejs', name='nodejs'),
    url(r'^reference/python/$', 'TechWise.views.python', name='python'),
    url(r'^reference/django/$', 'TechWise.views.django', name='django'),
    url(r'^reference/ruby/$', 'TechWise.views.ruby', name='ruby'),
    url(r'^reference/db2/$', 'TechWise.views.db2', name='db2'),
    url(r'^reference/mangodb/$', 'TechWise.views.mangodb', name='mangodb'),
    url(r'^reference/postgresql/$', 'TechWise.views.postgresql', name='postgresql'),
    url(r'^reference/mysql/$', 'TechWise.views.mysql', name='mysql'),
    url(r'^reference/sqlite/$', 'TechWise.views.sqlite', name='sqlite'),
    url(r'^reference/hadoop/$', 'TechWise.views.hadoop', name='hadoop'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
