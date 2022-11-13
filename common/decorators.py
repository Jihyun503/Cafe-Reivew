from django.shortcuts import redirect
from .models import User

def login_required(func):
    def wapper(request, *arg, **kwargs):
        login_session = request.session.get("user", "")

        if login_session == '':
            request.session['login_session'] = False
            return func(request, *arg, **kwargs)
        else:
            request.session['login_session'] = True
            return func(request, *arg, **kwargs)

        #return func(request, *arg, **kwargs)

    return wapper

