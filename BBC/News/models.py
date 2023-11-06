from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length = 100)
    content = models.TextField(max_length=5000)
    reporter = models.CharField(max_length = 100)
    image = models.ImageField(upload_to= 'product_images')
    date_reported = models.DateField()


    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.name