# Generated by Django 4.1.3 on 2023-01-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holder',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]
