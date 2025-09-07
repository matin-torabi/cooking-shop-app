from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

def move_user_to_group(username , group_name):
    User = get_user_model()
    user = User.objects.get(username=username)  # Fetch the user object
    group, _ = Group.objects.get_or_create(name=group_name)
    user.groups.set([group])  # Assign the group