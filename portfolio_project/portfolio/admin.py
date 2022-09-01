from django.contrib import admin

# Register your models here.
from .models import Projects, Skill_Category, Skills

admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(Skill_Category)