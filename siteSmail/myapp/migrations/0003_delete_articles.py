# Generated by Django 5.0.2 on 2024-05-07 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_articles_delete_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Articles',
        ),
    ]
