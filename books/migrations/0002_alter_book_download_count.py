# Generated by Django 4.2 on 2024-03-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='download_count',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
