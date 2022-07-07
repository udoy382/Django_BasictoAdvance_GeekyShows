from django.shortcuts import render

# Create your views here.


# ************* Page Counter **************


def home(request):
    ct = request.session.get('count', 0)
    new_count = ct + 1
    request.session['count'] = new_count
    return render(request, 'pagecounter/home.html', {'c':new_count})