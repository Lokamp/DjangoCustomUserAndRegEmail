
from django.contrib import admin
from django.urls import path

from users.views import logout_view, registration_company_view, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration_company_view, name='registration'),
]
