# Generated by Django 5.2.3 on 2025-06-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='earring',
            name='color',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='bottom',
            name='color',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='top',
            name='color',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
