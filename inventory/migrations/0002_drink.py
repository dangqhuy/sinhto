# Generated by Django 2.0.6 on 2018-06-12 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=0, max_digits=7)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='inventory.Shop')),
            ],
        ),
    ]