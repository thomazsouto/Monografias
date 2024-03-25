from django.db import models

class monografia(models.Model):
    
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano = models.CharField(max_length=255)
    orientador = models.CharField(max_length=255)
    resumo = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.titulo


