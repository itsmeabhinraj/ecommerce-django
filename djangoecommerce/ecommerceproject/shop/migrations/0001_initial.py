# Generated by Django 4.2.13 on 2024-06-27 21:12

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
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField(max_length=250)),
                ('price', models.DecimalField(decimal_places=True, max_digits=10)),
                ('img', models.ImageField(upload_to='gallery')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
