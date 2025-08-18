from django.db import models

class Planos(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    imagens = models.ImageField(upload_to='imagens_tom/')

    def __str__(self):
        return self.titulo