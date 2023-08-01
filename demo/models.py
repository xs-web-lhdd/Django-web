from django.db import models


# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField('添加字段时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        abstract = True


class User(CommonModel):
    """用户基本信息"""
    USER_STATUS = (
        (1, '正常'),
        (0, '删除')
    )
    username = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    nickname = models.CharField('用户昵称', max_length=64, null=True, blank=True)
    avatar = models.ImageField('用户头像', upload_to='avatar', null=True, blank=True)
    status = models.SmallIntegerField('用户状态', default=1, choices=USER_STATUS)
    is_super = models.BooleanField('是否为超级用户', default=False)

    # users = models.Manager()

    class Meta:
        db_table = 'demo_user'


class UserProfile(CommonModel):
    """用户详细信息"""
    SEX = (
        (1, '男性'),
        (0, '未知'),
        (2, '女性')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='关联用户')
    username = models.CharField('用户名', max_length=64, unique=True)
    real_name = models.CharField('真实姓名', max_length=64, null=True, blank=True)
    sex = models.SmallIntegerField('用户性别', default=0, choices=SEX)
    mamix = models.CharField('用户格言', max_length=128, null=True, blank=True)
    address = models.CharField('用户地址', max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'demo_user_profile'


class LoginHistory(models.Model):
    """用户的登陆历史"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_history', verbose_name='关联的用户')
    username = models.CharField('用户名', max_length=64)
    login_type = models.CharField('登陆平台', max_length=64)
    ip = models.CharField('IP地址', max_length=32, default='')
    ua = models.CharField('登陆的来源', max_length=512, default='')
    created_at = models.DateTimeField('登陆时间', auto_now_add=True)

    class Meta:
        db_table = 'demo_user_history'
        # 用登陆时间进行排序，默认从小到大，添加 - ，变为从大到小
        ordering = ['-created_at']
