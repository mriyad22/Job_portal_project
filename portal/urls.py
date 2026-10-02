from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),

    #-------------> User Authentication url
    path('register/', user_register, name='register_page'),
    path('login/', user_login, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    #-------------> User profile url
    path('profile/', profile, name='profile'),
    path('profile-update/', profile_update, name='profile_update'),

    #-------------> job CRUD operation url
    path('job-list/', jb_list, name='jb_list'),
    path('job-post/', jb_post, name='jb_post'),
    path('job-update/<int:u_id>/', jb_post_update, name='jb_update'),
    path('job-delete/<int:d_id>/', jb_post_delete, name='jb_delete'),

    #-------------> job apply url
    path('apply/<int:j_id>/', apply_job, name='apply_job'),

    #-------------> view my apply & all job candidate url
    path('my_applied/', my_applied, name='my_applied'),
    path('candidate/<int:c_id>/', candidete, name='candidate'),

    #-------------> password change url
    path("passwd-change/", passwd_change, name="passwd_change"),
]
