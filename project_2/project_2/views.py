from django.shortcuts import render

# E:\apron course\django\project_2\templates
def index(request):
    return render(request,'index.html')