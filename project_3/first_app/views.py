from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {'author': 'rohim' , "age" : 20,'list':["python","django","database","heroalom"],"birthday":datetime.datetime.now(),"val": " " ,"courses":[
        {
            "id" : 1,
            "name": "python",
            "fee" : 500,
        },
        {
            "id" : 2,
            "name": "programming hero",
            "fee": 2000
        },
        {
            "id" : 3,
            "name": "django",
            "fee": 3973
        },
        ]}
    return render(request,'home.html',d)
    # return render(request,'home.html',context=d)