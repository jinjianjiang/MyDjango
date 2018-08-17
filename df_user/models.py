from django.db import models

# Create your models here.
class UserInfo(models.Model):
    u_name = models.CharField(max_length=20)
    u_pwd = models.CharField(max_length=40)
    u_email = models.CharField(max_length=30)
    u_delivery = models.CharField(max_length=50, default='')
    u_address = models.CharField(max_length=100, default='')
    u_post = models.CharField(max_length=6, default='')
    u_phone = models.CharField(max_length=11, default='')

    class Meta():
        db_table = 'userinfo'  # 实现改变表的名字

    def __str__(self):
        return self.u_name