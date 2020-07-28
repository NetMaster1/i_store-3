from django.db import models
from app_goods.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    subject = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review=models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created',) 
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
    # def get_url(self):
    #     return reverse('product_detail', args=[self.id])
    def __Product__(self):
        return self.subject
