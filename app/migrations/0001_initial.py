# Generated by Django 4.1 on 2022-08-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('suitings', 'SUITINGS'), ('shirtings', 'SHIRTINGS'), ('khadi', 'KHADI'), ('colorkhadi', 'COLORKHADI'), ('linen', 'LINEN')], default='khadi', max_length=15)),
                ('price_range', models.IntegerField()),
                ('product_name', models.CharField(max_length=70)),
                ('fabric_type', models.CharField(choices=[('alpha', 'ALPHA'), ('magic', 'MAGIC'), ('bsy', 'BSY'), ('cotton', 'COTTON'), ('lycra', 'LYCRA'), ('metti', 'METTI')], default='magic', max_length=15)),
                ('design', models.CharField(choices=[('print', 'PRINT'), ('checks', 'CHECKS'), ('plane', 'PLANE')], default='plane', max_length=15)),
                ('color_chart', models.CharField(choices=[('sober', 'SOBER'), ('fancy', 'FANCY'), ('white', 'WHITE'), ('light', 'LIGHT'), ('dark', 'DARK')], default='sober', max_length=15)),
                ('product_image', models.URLField()),
                ('company', models.CharField(max_length=70)),
            ],
        ),
    ]
