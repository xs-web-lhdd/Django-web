from django.db import models


# Create your models here.

class CommonModel(models.Model):
    created_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        abstract = True


class User(CommonModel):
    """用户模型"""
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '帅哥'),
        ('0', '美女')
    ), default='1')
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    remark = models.CharField('备注', max_length=64, null=True, blank=True)
    email = models.EmailField('用户的邮箱', max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'user'


class Profile(CommonModel):
    """用户详细信息"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField('昵称', max_length=64)


