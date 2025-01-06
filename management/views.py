from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import permissions,authentication
from rest_framework.permissions import AllowAny
# Create your views here.


class UserView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=UserSerializer
    queryset=User.objects.all()

    def list(self, request, *args, **kwargs):
         
        users = User.objects.all()
        serializer=UserViewSerializer(users,many=True)
      
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=UserSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data='updated')
        else:
            return Response(data=serializer.errors)


class InstitutionView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=InstitutionSerializer
    queryset=InstitutionModel.objects.all()

    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=InstitutionSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data='updated')
        else:
            return Response(data=serializer.errors)

class DepartmentView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=DepartmentSerializer
    queryset=DepartmentModel.objects.all()

    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=DepartmentSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data='updated')
        else:
            return Response(data=serializer.errors)


class DivisionView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=DivisionSerializer
    queryset=DivisionModel.objects.all()

    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=DivisionSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data='updated')
        else:
            return Response(data=serializer.errors)

class ProductView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=ProductSerializer
    queryset=ProductModel.objects.all()

    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=ProductSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data='updated')
        else:
            return Response(data=serializer.errors)


class StudentView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def post(self,request,*args,**kw):
        id=kw.get('id')
        user=request.data.get('user')
        product=request.data.get('product')

        if StudentModel.objects.create(user_id=user,product_id=product,batch_id=id):
            return Response(data='added')
        else:
            return Response(data='error')
        
    def delete(self,request,*args,**kw):
        id=kw.get('id')
        student= StudentModel.objects.get(id=id)
        if student.delete():
            return Response(data='student removed')
        

class BatchView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=BatchSerializer
    queryset=BatchModel.objects.all()

    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=BatchSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data='updated')
        else:
            return Response(data=serializer.errors)
    

class MaterialView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=MaterialSerializer
    queryset=MaterialModel.objects.all()


class StudentBatchview(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,*args,**kw):
        id=kw.get('id')
        student=StudentModel.objects.filter(batch_id=id)
        serializer=StudentSerializer(student,many=True)
        return Response(data=serializer.data)
    
class UserInBatch(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,*args,**kw):
        id=kw.get('id')
        student=StudentModel.objects.filter(user_id=id)
        serializer=StudentSerializer(student,many=True)
        return Response(data=serializer.data)
    
class UserNotIn(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=UserSerializer
    queryset=User.objects.all()

    def list(self, request, *args, **kwargs):
        users = User.objects.filter(studentmodel__isnull=True)
        serializer=UserSerializer(users,many=True)
      
        return Response(data=serializer.data)
    

class StudentMaterial(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        id=kwargs.get('id')
        student=ProductModel.objects.get(id=id)
        product=student.material.all()
        serializer=MaterialSerializer(product,many=True)
        return Response(data=serializer.data)



class BatchMaterial(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        id=kwargs.get('id')
        batch=BatchModel.objects.get(id=id)
        product=batch.product
        material=product.material
        serializer=MaterialSerializer(material,many=True)
        return Response(data=serializer.data)
    


# student views 

class StudentDetails(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=UserViewSerializer
    queryset=User.objects.all()

    def list(self, request, *args, **kwargs):
         id=request.user.id
         user= User.objects.get(id=id)
         serializer=UserViewSerializer(user)
         return Response(data=serializer.data)

class UserLoginChackView(ModelViewSet):
    permission_classes=[AllowAny]

    serializer_class=UserSerializer
    queryset=User.objects.all()

class StudentviewBatch(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user=request.user.id
        batch=StudentModel.objects.filter(user_id=user)
        serializer=StudentSerializer(batch,many=True)
        return Response(data=serializer.data)


class StudentViewMaterial(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id=kwargs.get('id')
        batch=BatchModel.objects.get(id=id)
        product=batch.product
        material=product.material
        serializer=MaterialSerializer(material,many=True)
        return Response(data=serializer.data)

class StudentSideUpdateUser(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance=User.objects.get(id=request.user.id)
        serializer=UserSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data='updated')
        else:
            return Response(data=serializer.errors)
        
        
class StudentSideInstitute(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
     
        Institute=InstitutionModel.objects.all()
        serializer=InstitutionSerializer(Institute,many=True)
        return Response(data=serializer.data)
    
class StudentSideDepartment(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
     
        department=DepartmentModel.objects.all()
        serializer=DepartmentSerializer(department,many=True)
        return Response(data=serializer.data)
    
class StudentSideDivision(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
     
        division=DivisionModel.objects.all()
        serializer=DivisionSerializer(division,many=True)
        return Response(data=serializer.data)