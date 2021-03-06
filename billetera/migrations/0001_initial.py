# Generated by Django 3.0.2 on 2020-01-16 13:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=0, max_digits=8)),
                ('ingresos', models.IntegerField()),
                ('gastos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(2, 'Ingreso'), (1, 'Gasto')], default=1)),
                ('monto', models.DecimalField(decimal_places=0, max_digits=8)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billetera.Categoria')),
            ],
        ),
    ]
