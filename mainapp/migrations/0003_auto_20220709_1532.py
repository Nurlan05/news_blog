# Generated by Django 2.2.16 on 2022-07-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20220709_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['id'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='is Publish?'),
        ),
    ]
