from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=200,default="")
    image = models.ImageField(upload_to='category_images',blank=True,null=True) 
    
    def __str__(self):
        return self.title
    


class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    category = models.ForeignKey("Category", related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,null=True,blank=True,editable=False)
    updated_on = models.DateTimeField(auto_now= True)
    price = models.FloatField()
    description = models.TextField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['item','size'],
                name='unique_prod_color_size_combo'
            )
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog',kwargs={'slug':self.slug})

    def unique_slug(self):
        slug=slugify(self.title.replace('ı','i'))
        unique_slug=slug
        counter = 1
        while Item.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,counter)
            counter+=1
        return unique_slug
    
    def save(self,*args,**kwargs):
        self.slug = self.unique_slug()
        return super(Item,self).save(*args,**kwargs)

    class Meta:
        ordering = ['-created_on']


