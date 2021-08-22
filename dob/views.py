from datetime import datetime
from django.shortcuts import render


def index(request):
    return render(request, 'dob/hello_user.html')


def hello(request):
    if request.method == 'POST':
        # Reading UI inputs
        name = request.POST['username']
        birth_date = request.POST['datetime']

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday = datetime.strptime(birth_date, '%Y-%m-%d').weekday()
        weekday = days[weekday]

        message = f'Hi {name}, you were born on a {weekday}!'
        return render(request, 'dob/welcome_user.html',
            {'message': message, 'baseurl': 'https://deploy-spryte-demo.herokuapp.com/'})
