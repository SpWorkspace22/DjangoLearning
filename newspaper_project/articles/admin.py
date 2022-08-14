from django.contrib import admin

# Register your models here.
from .models import Article, Comments

class CommentInline(admin.TabularInline): # new
    model = Comments

class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [ CommentInline,]

admin.site.register(Article, ArticleAdmin) # new
admin.site.register(Comments)
