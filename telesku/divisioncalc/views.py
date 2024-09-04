from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def div(request):

	# val1 = request.GET['num1']
	# val2 = request.GET['num2']
	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])
	res = val1/val2
	opr = "/"
	equ = "="
	name = "Division"

	return render(request, "div.html", {'name':name, 'res':res, 'val1':val1, 'val2':val2, 'opr':opr, 'equ':equ})