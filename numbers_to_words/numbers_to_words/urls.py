from django.contrib import admin
from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('converter/', include('converter.urls')),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('converter.urls')),  # Замените 'converter' на имя вашего приложения, если оно отличается
]
