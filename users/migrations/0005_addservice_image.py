# Generated by Django 3.0.4 on 2020-04-06 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_addservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='addservice',
            name='image',
            field=models.ImageField(blank=True, upload_to='servicepic/'),
        ),
    ]
