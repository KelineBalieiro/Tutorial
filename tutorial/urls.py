from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path('schema/', schema_view),
]
