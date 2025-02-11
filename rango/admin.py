from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class PageInline(admin.StackedInline):
    model = Page
    extra = 1 # 额外一个空的表单

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category Info',               {'fields': ['name']}),
        ('Community', {'fields': ['views', 'likes'], 'classes': ['collapse']}),
    ]
    #  让 Page 作为 Category 的 Inline
    inlines = [PageInline]

    list_display = ('name', 'views', 'likes')
    #list_filter = ['views']

    prepopulated_fields = {'slug': ('name',)}



class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('details', {'fields': ['title', 'url', 'views']}),
    ]

    list_display = ('title', 'category', 'url')
    #list_filter = ['views']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
