# Generated by Django 4.1.5 on 2023-01-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_homebest_name6'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeGet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name7', models.CharField(max_length=100, verbose_name='Homeget name7')),
                ('name8', models.CharField(max_length=100, verbose_name='Homeget name8')),
                ('name9', models.CharField(max_length=100, verbose_name='Homeget name9')),
            ],
        ),
    ]
