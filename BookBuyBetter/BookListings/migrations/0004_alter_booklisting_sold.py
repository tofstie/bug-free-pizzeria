# Generated by Django 4.0.1 on 2022-01-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListings', '0003_alter_booklisting_bookimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklisting',
            name='Sold',
            field=models.BooleanField(default=False),
        ),
    ]