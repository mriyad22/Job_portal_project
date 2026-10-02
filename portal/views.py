from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Registered Succesfully')
            return redirect('login_page')
        
    form_data = RegisterForm()
    con = {
        'data' : form_data
    }

    return render(request, 'auth/register.html', con)


def user_login(request):
    if request.method == 'POST':
        form_data = LoginForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            messages.success(request, 'Loged in Succesfully')
            return redirect('home')
        
    form_data = LoginForm()
    con = {
        'data' : form_data
    }

    return render(request, 'auth/login.html', con)


@login_required
def logout_page(request):
    logout(request)

    return redirect('login_page')




def profile(request):

    return render(request, 'profile.html')


def profile_update(request):
    if request.user.user_type == 'Recruiter':
        try:
            user = request.user.recruiter_profile
        except RecruiterProfileModel.DoesNotExist:
            user = None

        if request.method == 'POST':
            form_data = RecProUpdateForm(request.POST, request.FILES, instance = user)
            if form_data.is_valid():
                data = form_data.save(commit=False)
                data.recruiter = request.user
                data.save()
                messages.success(request, 'User Data Updated')
                return redirect('profile')
            
        form_data = RecProUpdateForm(instance = user)

    else:
        try:
            user = request.user.seeker_profile
        except SeekerProfileModel.DoesNotExist:
            user = None

        if request.method == 'POST':
            form_data = SeekProUpdateForm(request.POST, request.FILES, instance = user)
            if form_data.is_valid():
                data = form_data.save(commit=False)
                data.seeker = request.user
                data.save()
                messages.success(request, 'User Data Updated')
                return redirect('profile')
            
        form_data = SeekProUpdateForm(instance = user)

    con = {
        'data' : form_data
    }

    return render(request, 'profile-update.html', con)




def jb_post(request):
    if request.method == 'POST':
        form_data = JobPostForm(request.POST)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.posted_by = request.user.recruiter_profile
            post.save()
            messages.success(request, 'Job has been Posted')
            return redirect('jb_list')
        
    form_data = JobPostForm()
    con = {
        'data' : form_data
    }

    return render(request, 'jobs/jb-post.html', con)




def jb_post_update(request, u_id):
    update_id = get_object_or_404(JobPostModel, id = u_id)
    if request.method == 'POST':
        form_data = JobPostForm(request.POST, instance = update_id)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Job has been updated')
            return redirect('jb_list')
        
    form_data = JobPostForm(instance = update_id)
    con = {
        'data' : form_data
    }

    return render(request, 'jobs/jb-post.html', con)




def jb_post_delete(request, d_id):
    delete_id = get_object_or_404(JobPostModel, id = d_id)
    if request.method == 'POST':
        delete_id.delete()
        messages.success(request, 'Job has been deleted')
        return redirect('jb_list')
    

    con = {
        'object' : delete_id
    }

    return render(request, 'delete.html', con)




def home(request):
    cate_data = CategoryModel.objects.all()

    con = {
        'data' : cate_data
    }

    return render(request, 'home.html', con)




def jb_list(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'Recruiter':
            data = JobPostModel.objects.filter(posted_by = request.user.recruiter_profile)
        else:
            data = JobPostModel.objects.all()
    else:
        data = JobPostModel.objects.all()

        if request.method == 'GET':
            cat = request.GET.get('cate_id')
            if cat:
                data = JobPostModel.objects.filter(category = cat)

    con = {
        'data' : data
    }

    return render(request, 'jobs/jb-list.html', con)



@login_required
def apply_job(request, j_id):
    jb_apl = get_object_or_404(JobPostModel, id = j_id)
    if request.method == 'POST':
        form_data = JobApplyForm(request.POST, request.FILES)
        if form_data.is_valid():
            apply = form_data.save(commit=False)
            apply.jb_applyer = request.user.seeker_profile
            apply.applied_by = jb_apl
            apply.save()
            messages.success(request, 'Job has been Posted')
            return redirect('jb_list')
        
    form_data = JobApplyForm()
    con = {
        'data' : form_data
    }

    return render(request, 'jb-apply.html', con)




def my_applied(request):
    my_apld = JobApplyModel.objects.filter(jb_applyer = request.user.seeker_profile)
    con = {
        'data' : my_apld
    }

    return render(request, 'my-applied.html', con)




def candidete(request, c_id):
    ca_apl = get_object_or_404(JobPostModel, id = c_id)

    cand = JobApplyModel.objects.filter(applied_by = ca_apl)

    con = {
        'data': cand
    }

    return render(request, 'candidate.html', con)




from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def passwd_change(request):
    if request.method == 'POST':
        form_data = PasswordChangeForm(request.user, request.POST)
        if form_data.is_valid():
            data = form_data.save()
            update_session_auth_hash(request, data)
            messages.success(request, 'Passwd has been changed')
            return redirect('profile')
        
    form_data = PasswordChangeForm(request.user)
    con = {
        'data' : form_data
    }

    return render(request, 'jobs/jb-post.html', con)