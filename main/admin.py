from django.contrib import admin
from main.models import Category,Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','created_on','slug','price',]
    list_display_links = ['created_on']
    list_filter = ['created_on']
    search_fields = ['title','description']
    list_editable = ['title']
    class Meta:
        model = Item

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = [
        'pk',
        'title',
        'slug',
    ]
    class Meta:
        model= Category


admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)