from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Sight(models.Model):
    """景点表"""
    name = models.CharField('景点名称', max_length=64)
    address = models.CharField('景点地址', max_length=64)
    comments = GenericRelation('Comment', related_query_name='sight_comments')


class Order(models.Model):
    """订单表"""
    # order = Order()
    # comments = order.comments
    sn = models.CharField('订单号', max_length=64)
    amount = models.FloatField('订单金额')
    comments = GenericRelation('Comment', related_query_name='order_comments')


# class SightComment(models.Model):
#     """景点评论"""
#     content = models.CharField('评论内容', max_length=512)
#     score = models.FloatField('分数', default=5)
#
#
# class OrderComment(models.Model):
#     """订单评论"""
#     content = models.CharField('评论内容', max_length=512)
#     score = models.FloatField('分数', default=5)


class Comment(models.Model):
    """所有评论"""
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('分数', default=5)
