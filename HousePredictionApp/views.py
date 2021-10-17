from django.shortcuts import render
from django.core.paginator import Paginator
from .models import HousePrice
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sn 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score

# Create your views here.

def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")
    
def result(request):
    dt = pd.read_csv(r'F:\Project and Thesis\Project\Django Project\ML Django Project\House Price Prediction Using ML in Django\USA_Housing.csv')
    dt = dt.drop(['Address'], axis=1)
    x = dt.drop('Price', axis=1)
    y = dt['Price']
    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=.30)
    model = LinearRegression()
    model.fit(xtrain, ytrain)

    if request.method == "POST":
        n1 = float(request.POST['n1'])
        n2 = float(request.POST['n2'])
        n3 = float(request.POST['n3'])
        n4 = float(request.POST['n4'])
        n5 = float(request.POST['n5'])

        pred = model.predict(np.array([n1,n2,n3,n4,n5]).reshape(1,-1))
        pred = round(pred[0])

        price = "The predict price is $ "+str(pred)

        data = HousePrice(AvgAreaIncome=n1,AvgAreaHouseAge=n2,AvgAreaNumberofRooms=n3,AvgAreaNumberofBedrooms=n4,AreaPopulation=n5,predict=pred)
        data.save()

    return render(request, "predict.html", {'result':price})
    

def record(request):
    data = HousePrice.objects.all()
    paginator = Paginator(data, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"record.html",{'page_obj':page_obj})