from django.db import models
class Modifier(models.Model):
    id = models.AutoField(primary_key=True,db_column="id")
    description = models.CharField(unique=True,max_length=10000)

    def __str__(self):
        return self.id

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500,unique=True)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.id

class Item(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    name = models.CharField(max_length=500,unique=True)
    description = models.CharField(max_length=10000)
    price = models.DecimalField(decimal_places=10,max_digits=60)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,related_name='items')
    modifiers = models.ManyToManyField(Modifier, blank=True, related_name='item', symmetrical=False)