from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # n

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login1, name='login' ),
    url(r'^sell/', views.submit_sale, name='submit_sale' ),
    url(r'^buy/', views.show_buy, name='show_buy' ),
    url(r'^register', views.register, name= 'register'),
    url(r'^logout/', views.logout1, name='logout'),
    path('makeorder/<str:article_id>/<str:article_reside>', views.makeorder, name='makeorder'),
    path('upload/', views.FileUploadView.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)