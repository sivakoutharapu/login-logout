# Generated by Django 5.0 on 2023-12-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('carona_status', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
    ]