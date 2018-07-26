from django.urls import path
from .views import list_todo,new_list,edit_list,delete_list

urlpatterns =[

    path('',list_todo, name='list_todo'),
    path('new/', new_list ,name='todolist_new'),
    path('edit/<int:id>', edit_list, name='todolist_edit'),
    path('delete/<int:id>', delete_list, name='todolist_delete'),

]

