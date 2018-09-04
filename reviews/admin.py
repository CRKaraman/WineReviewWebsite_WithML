from django.contrib import admin
from .models import Wine, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 3

class WineAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['user_name']
    list_filter = ['review']
    list_display = ('id','name')



admin.site.register(Wine,WineAdmin)
admin.site.register(Review)
