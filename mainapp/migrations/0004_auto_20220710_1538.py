# Generated by Django 2.2.16 on 2022-07-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20220709_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Tarix'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.FileField(blank=True, upload_to='', verbose_name='News image'),
        ),
    ]
