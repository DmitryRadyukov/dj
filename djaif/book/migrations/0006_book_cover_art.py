# Generated by Django 3.0.5 on 2020-04-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_first_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_art',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
