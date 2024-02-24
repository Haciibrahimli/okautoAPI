from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.generator import Generator
from services.uploader import Uploader
from django.contrib.auth import get_user_model 
from services.extract import extract_google_maps_url_from_iframe


SOCIAL_CHOICES = (
    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp", "WhatsApp"),
    ("twitter", "Twitter"),
    ("linkedin", "Linkedin"),
    ("tiktok", "Tiktok")
)






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


class About(DateMixin):
   title = models.CharField(max_length = 255,verbose_name = "bashliq")
   text = models.TextField(verbose_name = "metn")
   image  = models.ImageField(upload_to=Uploader.upload_photo_about,null=True,blank=True)
   questions = models.CharField(max_length = 255, verbose_name = "verilen suallar")
   answers = models.CharField(max_length = 255, verbose_name = "cavblar")
   info = models.TextField(verbose_name = "haqqimizda melumatlar")

   def __str__(self):
      return self.title
   
   class Meta:
      ordering = ("created_at",)
      verbose_name = "haqqimizda"
      verbose_name_plural = "haqqimizdakilar"

class Blog(DateMixin,SlugMixin):
   title = models.CharField(max_length = 255,verbose_name = "bashliq")
   text = models.TextField(verbose_name = "metn")
   image = models.ImageField(upload_to=Uploader.upload_photo_blog,null=True,blank=True)

   def __str__(self):
      return self.title
   
   class Meta:
      ordering = ("created_at",)
      verbose_name = "blog"
      verbose_name_plural = "bloglar"
      
   def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_= Blog)
        super(Blog, self).save(*args, **kwargs)


class Contact(DateMixin,SlugMixin):
    name = models.CharField(max_length=255,verbose_name='ad ve soyad')
    email = models.CharField(max_length=255,verbose_name='email adress')
    subject = models.CharField(max_length=255,verbose_name='movzu')
    mesage = models.TextField(verbose_name='mesaj')
    
    
   
    def __str__(self):
        return self.name
    
    class Meta:

     ordering = ('name',)
     verbose_name = 'contact'
     verbose_name_plural = 'contactlar'



    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Contact)
        super(Contact, self).save(*args, **kwargs)

class MainDetails(SlugMixin, DateMixin):
    email = models.EmailField(verbose_name='Email')
    adresss = models.CharField(max_length = 255,verbose_name='adress' )
    phones = models.CharField(max_length = 255,verbose_name='phones')
    locations = models.TextField(verbose_name='locations',null=True,blank=True)
    name = models.CharField(max_length = 255, verbose_name = 'adi')
    voen = models.CharField(max_length = 255,verbose_name = "voen nomresi")
    voen_adress = models.CharField(max_length = 255, verbose_name = "voen unvani")
  
    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "elaqe melumati"
        verbose_name_plural = "elaqe melumatlari"
        


    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=MainDetails)
        super(MainDetails, self).save(*args, **kwargs)

class SosialMedia(DateMixin):
    sosial_name = models.CharField(max_length=255,verbose_name='sosial media hesabi',choices=SOCIAL_CHOICES)
    sosial_link = models.TextField(verbose_name='sosial media linki')

    def __str__(self):
        return self.sosial_name

    class Meta:
        ordering = ("sosial_name", )
        verbose_name = "sosial media hesabi"
        verbose_name_plural = "sosial media hesablari"