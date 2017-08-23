"""TestingSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from APP1.views import hello_world
from APP1.views import Home
from APP1.views import GetDataPage
from APP1.views import YoutubeDownload
urlpatterns = [
               #url(r'^admin/', admin.site.urls),
               #url(r'^hi/', hello_world),
               #url(r'^Home/', Home),
               #url(r'^InputData/(?P<Get_1>\w+)/(?P<Get_2>[0-9A-Za-z ]+)/$', GetDataPage),
    url(r'^YoutubeDownload/(?P<Url>\w*)/$', YoutubeDownload),
    url(r'^YoutubeDownload/$', YoutubeDownload),
]
