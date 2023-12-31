# Generated by Django 4.2.1 on 2023-08-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInfo',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('content', models.TextField(default='用户暂未添加描述', null=True, verbose_name='描述')),
                ('status', models.BooleanField(choices=[(True, 'completed'), (False, 'uncompleted')], verbose_name='状态')),
                ('createTime', models.DateTimeField(verbose_name='创建时间')),
                ('endTime', models.DateField(null=True, verbose_name='结束时间')),
            ],
        ),
    ]
