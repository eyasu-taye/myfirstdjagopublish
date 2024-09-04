from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
	# pass
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, 'home.html')
def addc(request):
	# pass
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, 'add.html', {'name':"Addtion"})
def subc(request):
	# pass
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, 'sub.html', {'name':"Sustraction"})
def multc(request):
	# pass
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, 'mult.html', {'name':"Multiplacation"})
def divc(request):
	# pass
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, 'div.html', {'name':"Division"})




# def add(request):

# 	# val1 = request.GET['num1']
# 	# val2 = request.GET['num2']
# 	val1 = int(request.POST['num1'])
# 	val2 = int(request.POST['num2'])
# 	res = val1+val2
# 	opr = "+"
# 	equ = "="

# 	return render(request, "home.html", {'res':res, 'val1':val1, 'val2':val2, 'opr':opr, 'equ':equ})
