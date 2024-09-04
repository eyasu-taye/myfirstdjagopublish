from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mult(request):

	# val1 = request.GET['num1']
	# val2 = request.GET['num2']
	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])
	res = val1*val2
	opr = "*"
	equ = "="
	name = "Multiplication"

	return render(request, "mult.html", {'name':name, 'res':res, 'val1':val1, 'val2':val2, 'opr':opr, 'equ':equ})