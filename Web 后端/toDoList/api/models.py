from django.db import models

STATUS_ITEMS = [
    (True, 'completed'),
    (False, 'uncompleted')
]

# Create your models here.
class ItemInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, verbose_name='标题')
    content = models.TextField(null=True, default='用户暂未添加描述', verbose_name='描述')
    status = models.BooleanField(choices=STATUS_ITEMS, verbose_name='状态')
    createTime = models.DateTimeField(null=False, verbose_name='创建时间')
    endTime = models.DateField(null=True, verbose_name='结束时间')
