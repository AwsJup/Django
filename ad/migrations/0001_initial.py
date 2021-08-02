# Generated by Django 3.2.5 on 2021-08-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('mileage', models.FloatField()),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=255)),
                ('used', models.BooleanField()),
            ],
        ),
    ]
