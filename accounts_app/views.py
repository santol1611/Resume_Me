from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import get_messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts_app.models import UserProfile
from .forms import UserRegistrationForm, UserForm, ProfileForm
from .models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # หลังจากเข้าสู่ระบบสำเร็จ ให้ redirect ไปยังหน้าโปรไฟล์ของผู้ใช้
            return redirect('accounts_app:profile_view', user_id=user.id)  
        else:
            # แสดงข้อความแจ้งเตือนเมื่อเข้าสู่ระบบไม่สำเร็จ
            return render(request, 'accounts_app/index.html', {'error': 'Username หรือ Password ไม่ถูกต้อง'})
    return render(request, 'accounts_app/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('accounts_app/register.html')
        else:
            messages.error(request, 'There were errors in your registration.')
    else:
        form = UserRegistrationForm()

    # เคลียร์ข้อความหลังจากแสดงแล้ว
    storage = get_messages(request)
    for _ in storage:
        pass  # ลูปผ่านเพื่อเคลียร์ข้อความทั้งหมด

    return render(request, 'accounts_app/register.html', {'form': form})

@login_required
def profile_view(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    context = {
        'profile_user': profile_user,
        'profile_user_id': profile_user.id,  # เพิ่ม ID ของ user
    }
    return render(request, 'accounts_app/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('accounts_app:login') # ส่ง user กลับไปหน้า login

@login_required
def edit_profile(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)

    # ตรวจสอบว่า UserProfile มีอยู่แล้วหรือไม่
    profile_user_profile, created = UserProfile.objects.get_or_create(user=profile_user)

    # รับข้อมูลจากฟอร์ม
    user_form = UserForm(request.POST or None, instance=profile_user)
    profile_form = ProfileForm(request.POST or None, instance=profile_user_profile)

    context = {
        "profile_user_id": profile_user.id,
        "user_form": user_form,
        "profile_form": profile_form,
    }

    if request.method == "POST":
        # ตรวจสอบว่าแบบฟอร์มถูกต้องหรือไม่
        if user_form.is_valid() and profile_form.is_valid():
            # บันทึกข้อมูลจากฟอร์ม UserForm
            user_form.save()

            # บันทึกข้อมูลจากฟอร์ม ProfileForm
            profile_form.save()

            # Redirect ไปยังหน้าโปรไฟล์
            return redirect('accounts_app:profile_view', user_id=profile_user.id)

    return render(request, "accounts_app/edit_profile.html", context)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@login_required
def chang_password(request, user_id):
    return

