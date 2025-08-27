from django.db import models

class item(models.Model):
    titulo = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    

    def __str__(self):
        return self.titulo  
          
