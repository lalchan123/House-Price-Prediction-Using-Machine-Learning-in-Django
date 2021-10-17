from django.contrib import admin
from .models import HousePrice
# Register your models here.
class HousePriceAdmin(admin.ModelAdmin):
    list_display = ('AvgAreaIncome','AvgAreaHouseAge','AvgAreaNumberofRooms','AvgAreaNumberofBedrooms','AreaPopulation','predict')
    list_filter = ('AvgAreaIncome',)

admin.site.register(HousePrice,HousePriceAdmin)