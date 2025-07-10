from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)  # adds time when model was first time added to DB
    updated_at = models.DateTimeField(auto_now=True)  # updates every time model field was changed