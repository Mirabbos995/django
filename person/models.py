from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True) # blank=True - pustoy bop qolmasligi kerak  # null=True - null bop qolmasligi kerak
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category',models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name