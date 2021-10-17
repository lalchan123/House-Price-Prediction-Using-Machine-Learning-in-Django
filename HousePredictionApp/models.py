from django.db import models

# Create your models here.

class HousePrice(models.Model):
    AvgAreaIncome = models.FloatField() 
    AvgAreaHouseAge = models.FloatField() 
    AvgAreaNumberofRooms = models.FloatField() 
    AvgAreaNumberofBedrooms = models.FloatField() 
    AreaPopulation = models.FloatField() 
    predict = models.FloatField(default=0)

