from django.db import models

# Create your models here.
class Product(models.Model):
	productname = models.CharField(max_length=250)
	productdescription = models.CharField(max_length=250)
	productimage=models.ImageField(upload_to='product/%Y/%m/%d',blank=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	stock=models.PositiveIntegerField()
	slug=models.CharField(max_length=200,default='product')
	class Meta:
		ordering = ('productname',)

	def __str__(self):
		return self.productname


