# Generated by Django 3.1.4 on 2022-10-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20221001_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
