from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    # Редирект с корневого URL на /redoc/
    path('', RedirectView.as_view(url='/redoc/', permanent=False)),
]
