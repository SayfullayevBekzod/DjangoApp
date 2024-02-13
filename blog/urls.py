from django.urls import path

from blog.views import home_page, AboutView, user_profile, post_create, post_detail, logout_view, login_view, \
    register_view, post_delete, post_update

app_name = 'blog'
urlpatterns = [
    path('', home_page, name="home-page"),
    path('about/', AboutView.as_view(), name="about-page"),
    path('user-post/<str:username>', user_profile, name="user-profile"),
    path('new-post/', post_create, name="new-post"),
    path('post-detail/<int:pk>', post_detail, name="post-detail"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login-page"),
    path('register/', register_view, name="register-page"),
    path('post-update/<int:pk>', post_update, name="post-update"),
    path('post-delete/<int:pk>', post_delete, name="post-delete"),

]
