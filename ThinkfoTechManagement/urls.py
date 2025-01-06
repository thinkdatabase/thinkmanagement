"""
URL configuration for ThinkfoTechManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from rest_framework.routers import DefaultRouter
from management.views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
router=DefaultRouter()


router.register('user',UserView,basename='user')
router.register('userlogin',UserLoginChackView,basename='userlogincheck')
router.register('institution',InstitutionView,basename='institution')
router.register('department',DepartmentView,basename='department')
router.register('division',DivisionView,basename='devision')
router.register('product',ProductView,basename='product')
router.register('batch',BatchView,basename='batch')
router.register('usernotin',UserNotIn,basename='usernotin')
router.register('material',MaterialView,basename='material')
router.register('student/detail',StudentDetails,basename='student-detail')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:id>/',StudentView.as_view(),name='student'),
    path('student/batch/<int:id>/',StudentBatchview.as_view(),name='studentbatch'),
    path('user/batch/<int:id>/',UserInBatch.as_view(),name='userinbatch'),
    path('batch/<int:id>/material/',BatchMaterial.as_view(),name='batchmaterial'),
    path('student/material/<int:id>/',StudentMaterial.as_view(),name='studentmaterial'),
    path('student/batchview',StudentviewBatch.as_view(),name='studentviewbatch'),
    path('student/view/material/<int:id>/',StudentViewMaterial.as_view(),name='studentviewmaterial'),
    path('student/update/profile/',StudentSideUpdateUser.as_view(),name='StudentSideUpdateUser'),

    path('token/', obtain_auth_token),
    path('student/institute',StudentSideInstitute.as_view(),name='StudentSideInstitute'),
    path('student/department',StudentSideDepartment.as_view(),name='StudentSideDepartment'),
    path('student/division',StudentSideDivision.as_view(),name='StudentSideDivision'),

    

]+router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)