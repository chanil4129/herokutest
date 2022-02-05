import imp
from django.urls import re_path
from LibraryApp import views

from django.conf.urls.static import static
from django.conf import settings

#경로설정

urlpatterns=[
    re_path(r'^client/$',views.Lib_Client_APi),
    re_path(r'^client/([0-9]+)$',views.Lib_Client_APi),

    re_path(r'^book/$',views.Lib_Book_APi),
    re_path(r'^book/([0-9]+)$',views.Lib_Book_APi),

    re_path(r'^SaveFile$',views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)