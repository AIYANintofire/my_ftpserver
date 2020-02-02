from django.shortcuts import render,HttpResponse,redirect

from wp1 import models
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,"html/index.html")
def down(request,filename):
    reg=models.File.objects.get(file=filename)
    reg.file.file.open()
    file=str(reg.file.file)
    reg=open(file,"rb")
    response=HttpResponse(reg)
    response["Content-Type"] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename='+filename
    return response

def upload(request):
    file = request.FILES.get('file')
    models.File.objects.create(file=file)
    return redirect('/')

def showall_view(request):
    files = models.File.objects.all()
    return render(request,'html/show.html',{'files':files})