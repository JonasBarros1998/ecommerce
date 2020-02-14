from django.contrib.auth.models import User

def update(username, password):
    self._user = User.objects.get(username = username)
    self._user.set_password(password)
    self._user.save()
