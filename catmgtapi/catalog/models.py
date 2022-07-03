from django.db import models

def upload_to(instance, filename):
  return 'posts/{filename}'.format(filename)


class Category(models.Model):
  # category_id = models.PositiveIntegerField()
  title = models.CharField(max_length=200, null=False)
  image = models.ImageField(upload_to ='category/',blank=True, null=True, max_length = 255)
  parent = models.CharField( max_length=200,null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('-updated_at',)

  def __str__(self):
    return str(self.title)


class Product(models.Model):
  # product_id = models.PositiveIntegerField()
  title = models.CharField(max_length=200, null=False, blank=False)
  image = models.ImageField(upload_to ='product/', blank=True, null=True, max_length = 255)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, max_length = 255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  
  class Meta:
    ordering = ('-updated_at',)
    
  def __str__(self):
    return str(self.title)



class Banner(models.Model):
  # banner_id = models.PositiveIntegerField()
  title = models.CharField(max_length=200, null=False)
  image = models.ImageField(upload_to ='banner/',blank=True, null=True, max_length = 255)
  link = models.CharField(max_length=200, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering = ('-updated_at',)
    
  def __str__(self):
    return str(self.title)