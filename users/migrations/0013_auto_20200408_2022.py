# Generated by Django 3.0.4 on 2020-04-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200408_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addneeds',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='addservice',
            name='isDelete',
        ),
        migrations.AddField(
            model_name='addneeds',
            name='isDeleteByOrderUser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addneeds',
            name='isDeleteByUser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addservice',
            name='isDeleteByOrderUser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addservice',
            name='isDeleteByUser',
            field=models.BooleanField(default=False),
        ),
    ]