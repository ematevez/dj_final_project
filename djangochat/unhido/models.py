from django.db import models

class Solicitud(models.Model):
    sol_id_autoincremental = models.AutoField(primary_key=True)
    fecha_sol = models.DateField(null=True, blank=True)
    unidad = models.TextField(max_length=30, null=True, blank=True)
    depto = models.TextField(max_length=30, null=True, blank=True)
    rubro = models.TextField(max_length=50, null=True, blank=True)
    objeto = models.TextField(max_length=200, null=True, blank=True)
    prioridad = models.TextField(max_length=20, null=True, blank=True)
    esp_tec = models.FileField(upload_to='media/tecnica')
    justifica = models.TextField(max_length=200, null=True, blank=True)
    valida = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.sol_id_autoincremental)+ ' ' + self.depto
    

class Items(models.Model):
    primer_modelo = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    nombre = models.TextField()
    u_medida = models.TextField()
    cant = models.FloatField()
    observa = models.TextField()
    
    def __str__(self):
        return self.primer_modelo + self.nombre
    