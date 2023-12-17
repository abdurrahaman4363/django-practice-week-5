from django.shortcuts import render,redirect
from first_app.forms import RegisterForm, UserChange
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
   if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                # form.save(commit=False)
                messages.success(request,"Accout Created Successfully.")
                # messages.warning(request,"warning.")
                # messages.info(request,"info.")
                form.save(commit=True)
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request,'signup.html',{'form':form})
   else:
       return redirect('profilepage')

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = name, password = password)
                if user is not None:
                    login(request,user)
                    return redirect('profilepage')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profilepage')

# def profile(request):
#     if request.user.is_authenticated:
#         return render (request,'profile.html',{'user':request.user})
#     else:
#         return redirect('loginpage')
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserChange(request.POST, instance = request.user)
            if form.is_valid():
                # form.save(commit=False)
                messages.success(request,"Accout Updated Successfully.")
                # messages.warning(request,"warning.")
                # messages.info(request,"info.")
                form.save(commit=True)
                print(form.cleaned_data)
        else:
            form = UserChange(instance = request.user)
        return render(request,'profile.html',{'form':form})
    else:
       return redirect('signuppage')

def signout(request):
    logout(request)
    return redirect('loginpage')

def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.cleaned_data['user'])
                return redirect('profilepage')
            
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'passwordChange.html',{'form':form})
    else:
        return redirect('loginpage')
def password_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profilepage')
            
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'passwordChange.html',{'form':form})
    else:
        return redirect('loginpage')

