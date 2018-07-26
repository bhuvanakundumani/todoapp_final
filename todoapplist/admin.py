from django.contrib import admin


# Register your models here.


from .models import Category,Todolist


admin.site.register(Todolist)
admin.site.register(Category)