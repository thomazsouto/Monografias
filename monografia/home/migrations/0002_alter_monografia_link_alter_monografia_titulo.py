# Generated by Django 4.0.5 on 2022-06-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='link',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='titulo',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
