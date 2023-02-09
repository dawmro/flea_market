from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# category model class
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


# item model class
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    crerated_at = models.DateTimeField(auto_now_add=True)

        # display name of item objects
    def __str__(self):
        return self.name