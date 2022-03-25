from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def jaddu(request):
    dict={'name':'dhoni'}
    return render(request,'jinaga.html',context=dict)
def condition(request):
    d={'a':69}
    return render(request,'condition.html',d)