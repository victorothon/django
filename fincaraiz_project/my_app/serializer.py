from rest_framework.serializers import ModelSerializer
from .models import * #Reviews, Transactions, PropertyTypes, States, Cities, Categories, Properties

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews 
        fields = ["id","feedback","rating","avatar"]

class TransactionsSerializer(ModelSerializer):
    class Meta:
        model = Transactions
        fields = ["id","slug","propertyTypes"]

class PropertyTypesSerializer(ModelSerializer):
    class Meta:
        model = PropertyTypes
        fields = ["id","slug"]

class StatesSerializer(ModelSerializer):
    class Meta:
        model = States
        fields = ["id","slug"]

class CitiesSerializer(ModelSerializer):
    class Meta:
        model = Cities
        fields = ["id","slug","zip","state"]

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ["id","slug"]

class PropertiesSerializer(ModelSerializer):
    class Meta:
        model = Properties
        fields = ["id","title","image","price","city","baths","beds","sqft","category"]
        