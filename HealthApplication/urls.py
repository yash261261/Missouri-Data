from django.conf.urls import include, url
from django.contrib import admin
from . import views as main_views
from Task.views import MissouriDataViews, MissouriDetailViews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^missouri/([0-9]+)', MissouriDetailViews.as_view(), name='missouri-details'),
    url(r'^missouri', MissouriDataViews.as_view(), name='missouri-data'),
    url(r'', main_views.homepage, name='homepage'),
]
