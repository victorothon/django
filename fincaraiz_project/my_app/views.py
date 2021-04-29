from django.shortcuts import render
from django.http import request , JsonResponse, Http404
#from .models import Reviews, Transactions, PropertyTypes, States, Cities, Categories, Properties
from .models import *
from django.views import View 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
#from .serializer import ReviewsSerializer, TransactionsSerializer, PropertyTypesSerializer, StatesSerializer, CitiesSerializer, CategoriesSerializer, PropertiesSerializer  
from .serializer import *
# Create your views here.

########################### REVIEWS #########################

class ListReviews(APIView):

    #[GET]
    def get(self, request):
        obj = Reviews.objects.all()
        serializer_obj = ReviewsSerializer(obj, many=True)
        return Response(serializer_obj.data)

    #[PUT]
    def post(self, request):
        data = request.data
        serializer_obj = ReviewsSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)    #rest_framework

class UpdateReviews(APIView):
    
    #obtención de objeto
    def get_object(self, id):
        try:
            obj = Reviews.objects.get(id=id)
            return obj
        except Reviews.DoesNotExist:
            raise Http404
    
    #[PUT]
    #actualiza el registro utilizando el id proporcionado 
    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = ReviewsSerializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
    
    #[PATCH]
    #actualiza el registro de manera parcial
    def patch(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = ReviewsSerializer(obj,data=data,partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    #[DELETE]
    #elimina el registro
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "The Review with id:{}, has been deleted".format(id)})

##################### TRANSACTIONS ###########################

class ListTransactions(APIView):

    #[GET]
    def get(self, request):
        obj = Transactions.objects.all()
        serializer_obj = TransactionsSerializer(obj, many=True)
        return Response(serializer_obj.data)

    #[PUT]
    def post(self, request):
        data = request.data
        serializer_obj = TransactionsSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)    #rest_framework

class UpdateTransactions(APIView):
    
    #obtención de objeto
    def get_object(self, id):
        try:
            obj = Transactions.objects.get(id=id)
            return obj
        except Transactions.DoesNotExist:
            raise Http404
    
    #[PUT]
    #actualiza el registro utilizando el id proporcionado 
    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = TransactionsSerializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
    
    #[PATCH]
    #actualiza el registro de manera parcial
    def patch(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = TransactionsSerializer(obj,data=data,partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    #[DELETE]
    #elimina el registro
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "The Transaction with id:{}, has been deleted".format(id)})

################### Property Types ###########################

class ListPropertyTypes(APIView):

    #[GET]
    def get(self, request):
        obj = PropertyTypes.objects.all()
        serializer_obj = PropertyTypesSerializer(obj, many=True)
        return Response(serializer_obj.data)

    #[PUT]
    def post(self, request):
        data = request.data
        serializer_obj = PropertyTypesSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)    #rest_framework

class UpdatePropertyTypes(APIView):
    
    #obtención de objeto
    def get_object(self, id):
        try:
            obj = PropertyTypes.objects.get(id=id)
            return obj
        except PropertyTypes.DoesNotExist:
            raise Http404
    
    #[PUT]
    #actualiza el registro utilizando el id proporcionado 
    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = PropertyTypesSerializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
    
    #[PATCH]
    #actualiza el registro de manera parcial
    def patch(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = PropertyTypesSerializer(obj,data=data,partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    #[DELETE]
    #elimina el registro
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "The PropertyType with id:{}, has been deleted".format(id)})

################## States ####################################

class ListStates(APIView):

    #[GET]
    def get(self, request):
        obj = States.objects.all()
        serializer_obj = StatesSerializer(obj, many=True)
        return Response(serializer_obj.data)

    #[PUT]
    def post(self, request):
        data = request.data
        serializer_obj = StatesSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)    #rest_framework

class UpdateStates(APIView):
    
    #obtención de objeto
    def get_object(self, id):
        try:
            obj = States.objects.get(id=id)
            return obj
        except States.DoesNotExist:
            raise Http404
    
    #[PUT]
    #actualiza el registro utilizando el id proporcionado 
    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = StatesSerializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
    
    #[PATCH]
    #actualiza el registro de manera parcial
    def patch(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = StatesSerializer(obj,data=data,partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    #[DELETE]
    #elimina el registro
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "The State with id:{}, has been deleted".format(id)})

############################### Cities #######################

class ListCities(APIView):

    #[GET]
    def get(self, request):
        obj = Cities.objects.all()
        serializer_obj = CitiesSerializer(obj, many=True)
        return Response(serializer_obj.data)

    #[PUT]
    def post(self, request):
        data = request.data
        serializer_obj = CitiesSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)    #rest_framework

class UpdateCities(APIView):
    
    #obtención de objeto
    def get_object(self, id):
        try:
            obj = Cities.objects.get(id=id)
            return obj
        except Cities.DoesNotExist:
            raise Http404
    
    #[PUT]
    #actualiza el registro utilizando el id proporcionado 
    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = CitiesSerializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
    
    #[PATCH]
    #actualiza el registro de manera parcial
    def patch(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = CitiesSerializer(obj,data=data,partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    #[DELETE]
    #elimina el registro
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "The Citie with id:{}, has been deleted".format(id)})

#####################    Categories ###########################

class ListCategories(APIView):

    #[GET]
    def get(self, request):
        obj = Categories.objects.all()
        serializer_obj = CategoriesSerializer(obj, many=True)
        return Response(serializer_obj.data)

    #[PUT]
    def post(self, request):
        data = request.data
        serializer_obj = CategoriesSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)    #rest_framework

class UpdateCategories(APIView):
    
    #obtención de objeto
    def get_object(self, id):
        try:
            obj = Categories.objects.get(id=id)
            return obj
        except Categories.DoesNotExist:
            raise Http404
    
    #[PUT]
    #actualiza el registro utilizando el id proporcionado 
    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = CategoriesSerializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
    
    #[PATCH]
    #actualiza el registro de manera parcial
    def patch(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = CategoriesSerializer(obj,data=data,partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    #[DELETE]
    #elimina el registro
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "The Categorie with id:{}, has been deleted".format(id)})

###################### Properties #############################

class ListProperties(APIView):

    #[GET]
    def get(self, request):
        obj = Properties.objects.all()
        serializer_obj = PropertiesSerializer(obj, many=True)
        return Response(serializer_obj.data)

    #[PUT]
    def post(self, request):
        data = request.data
        serializer_obj = PropertiesSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)    #rest_framework

class UpdateProperties(APIView):
    
    #obtención de objeto
    def get_object(self, id):
        try:
            obj = Properties.objects.get(id=id)
            return obj
        except Properties.DoesNotExist:
            raise Http404
    
    #[PUT]
    #actualiza el registro utilizando el id proporcionado 
    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = PropertiesSerializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
    
    #[PATCH]
    #actualiza el registro de manera parcial
    def patch(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = PropertiesSerializer(obj,data=data,partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save() 
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    #[DELETE]
    #elimina el registro
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "The Propertie with id:{}, has been deleted".format(id)})

#Handlers
#@csrf_exempt
#@api_view(['GET'])
#def Prop_Reviews(request):
#
#    if request.method == "GET":
#        obj = Reviews.objects.all()
#        data={"response":list(obj.values("id","feedback","rating","avatar"))}
#        return JsonResponse(data)
#    
#    elif request.method == "POST":
#        feedback = request.POST["feedback"]
#        rating = request.POST["rating"]
#        avatar = request.POST["avatar"]
#        obj = Reviews(feedback=feedback, rating=rating, avatar=avatar)
#        obj.save()
#        data={"response":{"id":obj.id, "feedback":obj.feedback, "rating":obj.rating, "avatar":obj.avatar}}
#        return JsonResponse(data)

#@csrf_exempt
#def Prop_Transactions(request):
#    if request.method == "GET":
#        obj = Transactions.objects.all()
#        data={"response":list(obj.values("id","slug","propertyTypes"))}
#        return JsonResponse(data)
#    
#    elif request.method == "POST":
#        slug = request.POST["slug"]
#        propertyTypes = request.POST["propertyTypes"]
#        obj = Transactions(slug=slug, propertyTypes=propertyTypes)
#        obj.save()
#        data={"response":{"id":obj.id, "slug":obj.slug, "propertyTypes":obj.propertyTypes}}
#        return JsonResponse(data)

   # elif request.method == "PUT":
        
   # elif request.method == "PATCH":

   #elif request.method == "DELETE":
       # id = request.DELETE["id"]
       # obj = Reviews.filter(id=id)
       # obj.delete()
       # return JsonResponse("register {} has been deleted".format(id))

#class ListTransactions(View):
#    def get(self,request):
#        obj = Transactions.objects.all()
#        data={"response":list(obj.values("id","slug","propertyTypes"))}
#        return JsonResponse(data)
#
#    def post(self,request):
#        slug = request.POST["slug"]
#        propertyTypes = request.POST["propertyTypes"]
#        obj = Transactions(slug=slug, propertyTypes=propertyTypes)
#        obj.save()
#        data={"response":{"id":obj.id, "slug":obj.slug, "propertyTypes":obj.propertyTypes}}
#        return JsonResponse(data)

   # def put(self, request):

   # def patch(self, request):

   # def delete(self, request):
    #    id = request.DELETE["id"]
    #   obj = Reviews.filter(id=id)
    #    obj.delete()
    #    return JsonResponse("register {} has been deleted".format(id))


