# Generated by Django 3.0.5 on 2020-05-15 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_list_item_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
