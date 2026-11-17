from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Detailing_Website.views import (
    HomePage,
    Service_Page,
    Contact_Page,
    BookNow,
    ourwork
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Homepage', HomePage, name='home'),
    path('Service-Page', Service_Page, name='services'),
    path('ContactPage', Contact_Page, name='contact'),
    path('BookNow', BookNow, name='BookNow'),
    path('About', ourwork, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )