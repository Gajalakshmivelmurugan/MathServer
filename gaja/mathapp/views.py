from django.shortcuts import render
def rectarea(request):
    context={}
    context['area'] = "0"
    context['a'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        a = request.POST.get('base','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('base=',a)
        print('height=',h)
        area = 2*int(a) * int(a)+4*int(a)*int(h)
        context['area'] = area
        context['a'] = a
        context['h'] = h
        print('Area=',area)
    return render(request,'mathapp/math.html',context)

