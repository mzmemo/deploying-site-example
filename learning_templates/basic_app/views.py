from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'text': 'Building to Impact',
        'number': 100,
        'my_date': '02-05-2009',
    }
    return render(request, 'basic_app/index.html', context)


def other(request):
    return render(request, 'basic_app/other.html' )

def relative(request):
    return render(request, 'basic_app/relative.html')