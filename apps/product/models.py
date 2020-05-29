from django.db import models

# Create your models here.

class Category(models.Model): 
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title       = models.CharField(max_length=30)
    keywords    = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image       = models.ImageField(blank=True, upload_to='images/')
    status      = models.CharField(max_length=10, choices=STATUS)
    slug        = models.SlugField()
    parent      = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return self.title

class Product(models.Model): 
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category    = models.ForeignKey(Category,on_delete=models.CASCADE) #many to one relationship with Category Model
    title       = models.CharField(max_length=30)
    keywords    = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price       = models.FloatField()
    amount      = models.IntegerField()
    min_amount  = models.IntegerField()
    detail      = models.TextField()
    image       = models.ImageField(blank=True, upload_to='images/')
    slug        = models.SlugField()
    status      = models.CharField(max_length=10, choices=STATUS)
    parent      = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return self.title
