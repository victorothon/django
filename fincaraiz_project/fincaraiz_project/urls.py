"""fincaraiz_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from my_app.views import *
#from my_app.views import ListReviews, UpdateReviews 
#from my_app.views import ListTransactions, UpdateTransactions
#from my_app.views import ListPropertyTypes, UpdatePropertyTypes
#from my_app.views import ListStates, UpdateStates
#from my_app.views import ListCities, UpdateCities
#from my_app.views import ListCategories, UpdateCategories
#from my_app.views import ListProperties, UpdateProperties

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listreviews/', ListReviews.as_view()),
    path('updatereviews/<id>', UpdateReviews.as_view()),
    path('listtransactions/', ListTransactions.as_view()),
    path('updatetransactions/<id>', UpdateTransactions.as_view()),
    path('listpropertytypes/', ListPropertyTypes.as_view()),
    path('updatepropertytypes/<id>', UpdatePropertyTypes.as_view()),
    path('liststates/', ListStates.as_view()),
    path('updatestates/<id>', UpdateStates.as_view()),
    path('listcities/', ListCities.as_view()),
    path('updatecities/<id>', UpdateCities.as_view()),
    path('listcategories/', ListCategories.as_view()),
    path('updatecategories/<id>', UpdateCategories.as_view()),
    path('listproperties/', ListProperties.as_view()),
    path('updateproperties/<id>', UpdateProperties.as_view())
]
