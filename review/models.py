from django.db import models

# Create your models here.
class Review(models.Model):
    bno = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=64, verbose_name="상호명")
    address = models.CharField(max_length=64, verbose_name="주소")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey('common.User', on_delete=models.CASCADE)
    write_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
