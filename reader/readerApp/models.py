from django.db import models

class Mahasiswa(models.Model):
   npm = models.CharField(max_length = 10,primary_key = True)
   nama = models.CharField(max_length = 50)
    class Meta:
        managed = False
        db_table = 'updateApp_mahasiswa'
