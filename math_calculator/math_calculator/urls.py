from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Функция для редиректа с "/" на "/calculator/"
def redirect_to_calculator(request):
    return redirect('/calculator/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator.urls')),  # Основной маршрут
    path('', redirect_to_calculator),  # Авто-редирект на /calculator/
]
