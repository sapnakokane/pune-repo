"""allpro URL Configuration

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
from app6 import views as v6
from app7 import views as v7
from app8 import views as v8
from app9 import views as v9
from app10 import views as v10
from app11 import views as v11
from app12 import views as v12
from app13 import views as v13
from app14 import views as v14
from app15 import views as v15
from app16 import views as v16
from app17 import views as v17
from app18 import views as v18

urlpatterns = [
    path('admin/', admin.site.urls),
    path('morn/',v1.morn),
    path('dtym/',v1.dtym),
    path('msgtym/',v1.msgtym),
    path('in/',include("extraapp.urls")),
    path('tempmsg/',v1.tempmsg),
    path('temptag/',v1.temptag),
    path('home/',v2.home),
    path('movies/',v2.movies),
    path('sports/',v2.sports),
    path('modlview/',v3.modlview),
    path('formview/',v4.formview),
    path('formview1/',v4.formview1),
    path('exview/',v5.formexview),
    path('reformview/',v6.reformview),
    path('feedbackview/',v7.feedbackview),
    path('signupview/',v7.signupview),
    path('botview/',v8.botview),
    path('smodlView/',v9.smodlView),
    path('smodlshow/',v9.smodlshow),
    path('Moviesview/',v10.Moviesview),
    path('blockview/',v11.blockview),
    path('tempfilview/',v12.tempfilview),
    path('index_view/',v13.index_view),
    path('count_view/',v13.count_view),
    path('cformview/',v13.cformview),
    path('datetimeview/', v13.date_time_view),
    path('resultview/', v13.result_view),
    path('name_view/', v14.name_view),
    path('age/', v14.age_view),
    path('gf/', v14.gf_view),
    path('result/', v14.result_view),
    path('index/', v15.index),
    path('add/', v15.additem),
    path('display/', v15.displayitem),
    path('pgcount/', v16.page_count_view),
    path('na/', v17.naview),
    path('age/', v17.agview),
    path('gf/', v17.gfview),
    path('re/', v17.resultvieww),
    path('adding/', v18.additemView),
    path('displaying/', v18.displayitemView),

]
