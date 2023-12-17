from django.urls import path
from first_app.views import home,signup,signin,profile,signout,password_change,password_change2

urlpatterns = [
    path('',home,name='homepage'),
    path('signup/',signup,name='signuppage'),
    path('login/',signin,name='loginpage'),
    path('profile/',profile,name='profilepage'),
    path('logout/',signout,name='logoutpage'),
    path('password_change/',password_change,name='password_change'),
    path('password_change2/',password_change2,name='password_change2'),
]
