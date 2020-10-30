from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # n

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.show_buy, name='show_buy' ),
    url(r'^login/', views.login1, name='login' ),
    url(r'^sell/', views.submit_sale, name='submit_sale' ),
    url(r'^register', views.register, name= 'register'),
    url(r'^account/', views.account, name='account'),
    url(r'^logout/', views.logout1, name='logout'),
    path('show_land/<str:id>', views.show_more, name='show_land'),
    path('makeorder/<str:article_id>/<str:article_reside>', views.makeorder, name='makeorder'),
    path('intereted-in/<str:id>', views.interest, name='interest'),
    path('upload/', views.FileUploadView.as_view()),
    path('delete-interest/<str:id>',views.delete_interest, name='delete_interest' ),
    path('delete-land/str<str:id>', views.delete_land, name='delete_land'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)