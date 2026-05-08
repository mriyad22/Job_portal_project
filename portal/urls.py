from django.urls import path
from .views import *

urlpatterns = [
    path('register/', user_register, name='register_page'),
    path('login/', user_login, name='login_page'),
    path('', home, name='home'),
    path('logout/', logout_page, name='logout_page'),

    path('profile/', profile, name='profile'),
    path('profile-update/', profile_update, name='profile_update'),

    path('job-list/', jb_list, name='jb_list'),
    path('job-post/', jb_post, name='jb_post'),
    path('apply/<int:j_id>/', apply_job, name='apply_job'),

    path('my_applied/', my_applied, name='my_applied'),
    path('candidate/<int:c_id>/', candidete, name='candidate'),

    path("passwd-change/", passwd_change, name="passwd_change"),
]
