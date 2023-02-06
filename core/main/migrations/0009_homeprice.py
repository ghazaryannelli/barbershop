# Generated by Django 4.1.5 on 2023-01-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_homeservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100, verbose_name='Homeprice name1')),
                ('name2', models.CharField(max_length=100, verbose_name='Homeprice name2')),
                ('name3', models.CharField(max_length=100, verbose_name='Homeprice name3')),
                ('name4', models.CharField(max_length=100, verbose_name='Homeprice name4')),
                ('name5', models.CharField(max_length=100, verbose_name='Homeprice name5')),
                ('name6', models.CharField(max_length=100, verbose_name='Homeprice name6')),
                ('name7', models.CharField(max_length=100, verbose_name='Homeprice name7')),
                ('img', models.ImageField(upload_to='media', verbose_name='Homeprice image')),
                ('price1', models.IntegerField(verbose_name='Homeprice price')),
                ('price2', models.IntegerField(verbose_name='Homeprice price')),
                ('price3', models.IntegerField(verbose_name='Homeprice price')),
                ('price4', models.IntegerField(verbose_name='Homeprice price')),
                ('price5', models.IntegerField(verbose_name='Homeprice price')),
            ],
        ),
    ]