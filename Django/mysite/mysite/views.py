# this file was crated by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')
# def text(request):
#     with open("E:/Python work/Django/Instrunctions.txt",'r') as f:
#         text_string=str(f.read())

    # return(HttpResponse(text_string))
def capitalize(request):
    return HttpResponse("capitalize  <br><b><a href='http://127.0.0.1:8000/'>GO BAck</a><b>")
def analyze(request):
    djtext=request.GET.get('text','default')
    remove=request.GET.get('remove','off')
   anayzed=djtext
   punc=''' /\.,><}{[]|:;?@!()""'''
    params={'perpouse':"Remove Punctuations","analyzed":"analyzed"}
    print(djtext)
    return render(request,"analyze.html",params)

def count(request):
    return HttpResponse("""Count cahracter  <br><b><a href='http://127.0.0.1:8000/'>GO BAck</a><b>""")

    