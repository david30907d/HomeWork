from django.contrib import admin
from demo.models import Fruit
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')

admin.site.register(Fruit, CourseAdmin)
