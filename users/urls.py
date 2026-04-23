from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
]

# users/urls.py

# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LogoutView 
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
      'logout/',
      # Прямо в описании обработчика укажем шаблон, 
      # который должен применяться для отображения возвращаемой страницы.
      # Да, во view-классах так можно! Как их не полюбить.
      LogoutView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
]
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    # Регистрация нового пользователя
    path('signup/', views.SignUp.as_view(), name='signup'),
]
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Регистрация
    path('signup/', views.SignUp.as_view(), name='signup'),
    # Вход и выход
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    # Смена пароля
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    # Восстановление пароля
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    # ⬇️ ЭТОТ МАРШРУТ НУЖЕН ДЛЯ ПЕРЕХОДА ПО ССЫЛКЕ ⬇️
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),          # ← добавить эту строку
    path('auth/', include('django.contrib.auth.urls')),  # ← оставить эту
    path('about/', include('about.urls', namespace='about')),
    path('', include('posts.urls', namespace='posts')),
]
