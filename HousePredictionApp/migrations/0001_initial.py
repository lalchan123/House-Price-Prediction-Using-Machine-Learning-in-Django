# Generated by Django 3.0.5 on 2021-09-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.FloatField()),
                ('n2', models.FloatField()),
                ('n3', models.FloatField()),
                ('n4', models.FloatField()),
                ('n5', models.FloatField()),
            ],
        ),
    ]