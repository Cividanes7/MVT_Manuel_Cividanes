# Generated by Django 4.1.3 on 2022-12-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
