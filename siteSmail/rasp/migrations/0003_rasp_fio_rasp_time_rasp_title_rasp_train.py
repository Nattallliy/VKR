# Generated by Django 4.2.7 on 2024-05-08 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rasp', '0002_alter_rasp_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='rasp',
            name='FIO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rasp.peoples'),
        ),
        migrations.AddField(
            model_name='rasp',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rasp.time'),
        ),
        migrations.AddField(
            model_name='rasp',
            name='title',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='rasp',
            name='train',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rasp.class'),
        ),
    ]
