from django.contrib.auth.models import User

def update(username, password):
    user = User.objects.get(username = username)
    user.set_password(password)
    user.save()
