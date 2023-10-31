from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        my_input_value = request.POST.get('my_input', 'Default Value')
    else:
        my_input_value = 'Default Value'
    
    context = {
        'variable': my_input_value
    }
    return render(request, 'index.html', context)
