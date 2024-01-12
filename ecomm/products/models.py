from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to="categories")
    slug=models.SlugField(unique=True,null=True,blank=True)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.category_name

class ColorVariant(BaseModel):
    color_name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name
    
    


class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    price=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.size_name

    



class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price=models.IntegerField()
    product_description=models.TextField()
    slug=models.SlugField(unique=True,null=True,blank=True)
    color_variant=models.ManyToManyField(ColorVariant,blank=True)
    size_variant=models.ManyToManyField(SizeVariant,blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.product_name)
        super(Product,self).save(*args,**kwargs)

    
    
    def get_product_price_by_size(self, size):
        try:
            size_variant = SizeVariant.objects.get(size_name=size)
            return size_variant.price
        except SizeVariant.DoesNotExist:
            return self.price
    def __str__(self) -> str:
        return self.product_name

class  ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")
    image=models.ImageField(upload_to="product")

class Coupon (BaseModel):
    coupon_code = models.CharField(max_length=10)
    is_expired = models.BooleanField(default=False)
    discount_price=models.IntegerField(default=100)
    minimum_amount=models.IntegerField(default=500)




