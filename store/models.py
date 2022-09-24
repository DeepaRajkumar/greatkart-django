from django.db import models
from category.models import Category
from django.urls import reverse
class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug        =models.SlugField(max_length=200,unique=True)
    description =models.TextField(max_length=350,blank=True)
    price       =models.IntegerField()
    images      =models.ImageField(upload_to='photos/products')
    stock       =models.IntegerField()
    is_available=models.BooleanField(default=True)
    category    =models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)
    def get_url(self):
        return reverse('products_detail',args=[self.category.slug,self.slug])
    def __str__(self):
        return self.product_name









# Create your models here.