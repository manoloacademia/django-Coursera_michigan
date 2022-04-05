from django.http import HttpResponse

# Create your views here.
# set a cookie and implement the session

def myview(request):
    print(request.COOKIES)
    resp = HttpResponse("Esta es la cookie que quiere la gente")
    resp.set_cookie('dj4e_cookie', '2b43d625', max_age=1000)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    return resp

