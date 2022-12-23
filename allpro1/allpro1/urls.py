"""allpro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views as v1
from app2 import views as v2
from app3 import views as v3
from app4 import views as v4
from app5 import views as v5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pgcnt/',v1.count_view),
    path('name/',v2.name_view),
    path('age/',v2.age_view),
    path('gf/',v2.gf_view),
    path('result/',v2.result_view),
    path('chkkkhome/',v3.home_view),
    path('python/',v3.python_view),
    path('java/',v3.java_view),
    path('apti/',v3.aptitude_view),
    path('logout/',v3.logout_view),
    path('signup/',v3.signup_view),
    path('accounts/',include('django.contrib.auth.urls')),
    path('chkkkkk',v4.retrive_view),
    path('create/',v4.create_view),
    path('delete/<int:id>/',v4.delete_view),
    path('update/<int:id>/',v4.update_view),
    path('',v5.BeerListView.as_view(),name='home'),
    path('<int:pk>/',v5.BeerDetailView.as_view(),name='detail'),
    path('createbeer/',v5.BeerCreateView.as_view()),
    path('updatebeer/<int:pk>/',v5.BeerUpdateView.as_view()),
    path('deletebeer/<int:pk>/',v5.BeerDeleteView.as_view()),
]
