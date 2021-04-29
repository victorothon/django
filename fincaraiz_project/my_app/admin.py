from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Reviews)
admin.site.register(models.Transactions)
admin.site.register(models.PropertyTypes)
admin.site.register(models.States)
admin.site.register(models.Cities)
admin.site.register(models.Categories)
admin.site.register(models.Properties)