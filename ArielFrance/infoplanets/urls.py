from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_infoplanetshtml),
    path('exoclockjson/', views.getexoclockdata),
    path('exoplanets/', views.planetTypeFilter),
    path('search_planet/', views.search_planet, name="search-planet"),
    path('<exoplanet_name>', views.show_exopl_info, name='show-exopl-info')
]