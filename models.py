from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,db_index=True, unique=True)


class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'



    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('mobileStore:product_list_by_category', args=[self.slug])







class Product(models.Model):
    name = models.CharField(max_length=100)
    Fullprice = models.DecimalField(max_digits=10, decimal_places=2)
    Discountprice = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/',blank=True)



    class Meta:
        ordering=('name',)
        index_together=('id',)#'slug')



    def __str__(self):
        return self.name


# def get_absolute_url(self):
#     return reverse('mobileStore:product_detail', args=[self.id, self.slug])
