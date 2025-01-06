from rest_framework import serializers
from .models import *




class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstitutionModel
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartmentModel
        fields='__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model=DivisionModel
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','username','password','phone','email','is_superuser','institute','department','divison']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserViewSerializer(serializers.ModelSerializer):
    institute=InstitutionSerializer()
    department=DepartmentSerializer()
    divison=DivisionSerializer()
    class Meta:
        model=User
        fields=['id','first_name','username','password','phone','email','is_superuser','institute','department','divison']

   



class BatchSerializer(serializers.ModelSerializer):

    class Meta:
        model=BatchModel
        fields=['name','product','id']

class StudentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    batch=BatchSerializer()

    class Meta:
        model=StudentModel
        fields='__all__'

    



class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model=MaterialModel
        fields=['id','title','description','file']
        

class ProductSerializer(serializers.ModelSerializer):
    material = serializers.PrimaryKeyRelatedField(
        many=True,queryset=MaterialModel.objects.all()
        
    )

    class Meta:
        model=ProductModel
        fields=['name','id','material']

    def create(self, validated_data):
        materials = validated_data.pop('material')   
        product = ProductModel.objects.create(**validated_data)  
        product.material.set(materials)
        return product


    # def update(self, instance, validated_data):
    #     # Extract nested material data
    #     materials_data = validated_data.pop('material')
    #     # Update product fields
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     # Clear and update materials
    #     instance.material.clear()
    #     for material_data in materials_data:
    #         material, created = MaterialModel.objects.get_or_create(**material_data)
    #         instance.material.add(material)
    #     return instance



