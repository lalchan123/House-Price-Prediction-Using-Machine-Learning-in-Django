# Generated by Django 3.0.5 on 2021-09-29 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HousePredictionApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houseprice',
            old_name='n1',
            new_name='AreaPopulation',
        ),
        migrations.RenameField(
            model_name='houseprice',
            old_name='n2',
            new_name='AvgAreaHouseAge',
        ),
        migrations.RenameField(
            model_name='houseprice',
            old_name='n3',
            new_name='AvgAreaIncome',
        ),
        migrations.RenameField(
            model_name='houseprice',
            old_name='n4',
            new_name='AvgAreaNumberofBedrooms',
        ),
        migrations.RenameField(
            model_name='houseprice',
            old_name='n5',
            new_name='AvgAreaNumberofRooms',
        ),
    ]