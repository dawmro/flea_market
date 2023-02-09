from django.db import models

# Create your models here.

# category database class
class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        # order category objects by name
        ordering = ('name',)
        # set plural for Category name
        verbose_name_plural = 'Categories'

    # display name of category objects
    def __str__(self):
        return self.name