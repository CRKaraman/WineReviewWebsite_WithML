from django.contrib import admin
from .models import Wine, Review,Cluster

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 3

class WineAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['user_name']
    list_filter = ['review']
    list_display = ('name','id')

class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']



admin.site.register(Wine,WineAdmin)
admin.site.register(Review)
admin.site.register(Cluster, ClusterAdmin)
