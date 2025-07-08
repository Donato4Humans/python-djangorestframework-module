from django.db import models

class UserModel(models.Model):
    class Meta:
        db_table = "users"
    name = models.CharField(max_length=20) # for small names, especially cyrillic max_length = 255 is optimal
    #name = models.TextField() for larger fields can be used TextField(much bigger volume)
    age = models.IntegerField()
    status = models.BooleanField(default=False)
    weight = models.FloatField()

