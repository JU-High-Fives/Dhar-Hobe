from django.urls import path, include
from . import views
# from . views import ShowProfilePageView, CreateProfilePageView, EditProfilePageView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
#     path('profile/<int:pk>', ShowProfilePageView.as_view(),
#          name='profile'),
#     path('<int:pk>/edit_profile_page/',
#          EditProfilePageView.as_view(), name='edit_profile_page'),
#     path('create_profile_page/', CreateProfilePageView.as_view(),
#          name='create_profile_page'),
]
