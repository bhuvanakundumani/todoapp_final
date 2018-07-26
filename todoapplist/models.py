from django.db import models

# Create your models here.

from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length =100)



    def __str__(self):
        return self.name

class Todolist(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now())
    due_date = models.DateField( help_text="Enter the date in the formatt YYYY-MM-DD")
    category = models.ForeignKey(Category, null = True, on_delete=models.CASCADE, default='general')

    def __str__(self):
        return self.title


        #' ' +self.content + ' ' + str( self.created )+ ' '+ str(self.due_date )+ ' '+ str(self.category)


    #





