from django.db import models

# Create your models here.



class Category(models.Model):

      #Property
      
      category_name = models.CharField(max_length=255) 
      
      category_quant = models.IntegerField() 
            
      #Constructor
      
      #Method
      def __str__(self):  #dunder method or magic method
          return self.category_name 
        
      #Nested class
      class Meta:
          #Prorerty
          verbose_name = 'Category' #singular
          verbose_name_plural = 'Categories'  #plural
          
          #Constructor
          
          #Method
          
          
          #Nested class
