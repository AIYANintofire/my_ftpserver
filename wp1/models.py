from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='file')
    class Meta:
        db_table='t_stu'
