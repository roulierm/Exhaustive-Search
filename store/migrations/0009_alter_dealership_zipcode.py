# Generated by Django 3.2.9 on 2021-11-29 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_dealership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealership',
            name='zipCode',
            field=models.IntegerField(verbose_name='zipCode'),
        ),
    ]
