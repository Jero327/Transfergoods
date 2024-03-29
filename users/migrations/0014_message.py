# Generated by Django 3.0.4 on 2020-04-09 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200408_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('msg_content', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
                ('author', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
