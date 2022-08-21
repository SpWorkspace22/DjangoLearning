from django.contrib import admin


# Register your models here.
from .models import Consume, Food


admin.site.register(Food)
admin.site.register(Consume)