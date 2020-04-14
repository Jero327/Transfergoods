# Generated by Django 3.0.4 on 2020-04-11 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200411_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='orderstatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='need_orderstatus', to='users.OrderStatus'),
        ),
        migrations.AlterField(
            model_name='service',
            name='orderstatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_orderstatus', to='users.OrderStatus'),
        ),
    ]