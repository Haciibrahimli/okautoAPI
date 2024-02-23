from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.generator import Generator
from services.uploader import Uploader
from django.contrib.auth import get_user_model 
from services.extract import extract_google_maps_url_from_iframe

class Index(DateMixin):
    title = models.CharField(max_length = 255,verbose_name = 'basliq')
    text = models.TextField(verbose_name = 'metn')
    slider_image = models.ImageField(upload_to=Uploader.upload_photo_index,null=True,blank=True)
    image = models.ImageField(upload_to=Uploader.upload_photo_index1,null=True,blank=True)


    def __str__(self):
        return self.title()

    
    class Meta:
     ordering = ('-created_at',)
     verbose_name = 'index'
     verbose_name_plural = 'index'

class Product(DateMixin,SlugMixin):
    name = models.CharField(max_length = 255,verbose_name = 'mehsulun adi')
    code = models.CharField(max_length = 255, verbose_name = 'mehsulun kodu') 
    price = models.FloatField(verbose_name = 'mehsulun qiymeti')
    discount_price = models.FloatField(verbose_name = 'mehsulun endirimli qiymeti')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "mehsul"
        verbose_name_plural = "mehsullar"


    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Product)
        super(Product, self).save(*args, **kwargs)



