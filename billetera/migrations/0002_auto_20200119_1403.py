# Generated by Django 3.0.1 on 2020-01-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billetera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='tipo',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Gasto', 'Gasto')], default='Gasto', max_length=10),
        ),
    ]
