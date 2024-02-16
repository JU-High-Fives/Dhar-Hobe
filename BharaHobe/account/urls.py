from django.urls import path
from . import views
from .views import ShowProfilePageView, CreateProfilePageView, EditProfilePageView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('profile/<int:pk>/edit/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('profile/create/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
