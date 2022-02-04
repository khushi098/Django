from django.db import models

# Create your models here.
class Project(models.Model):
    
      #Property
      
      project_name = models.CharField() 
      
    
            
      #Constructor
      
      #Method
      def __str__(self):  #dunder method or magic method
          return self.project_name 
        
      #Nested class
      pass