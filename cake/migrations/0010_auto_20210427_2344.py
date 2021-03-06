# Generated by Django 3.2 on 2021-04-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0009_auto_20210427_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='category',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cake',
            name='description',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cake',
            name='eggless',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cake',
            name='flavour',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cake',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cake',
            name='weight',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
