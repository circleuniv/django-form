import os
from django.shortcuts import render
from mysite import  settings

def index(request):
    return render(request,'index.html')

def tutorial(request):
    path=settings.STATICFILES_DIRS[0]
    img_list=os.listdir(path)
    # print(settings.BASE_DIR)
    # print(path)
    # print(img_list)
    context={"images":img_list}
    return render(request, 'tutorial.html',context)

