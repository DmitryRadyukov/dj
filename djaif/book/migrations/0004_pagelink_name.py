# Generated by Django 3.0.5 on 2020-04-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_pagelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelink',
            name='name',
            field=models.TextField(default='???'),
            preserve_default=False,
        ),
    ]