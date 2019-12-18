from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import voting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('voting.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_url=settings.STATIC_ROOT)