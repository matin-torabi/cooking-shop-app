# This is a group manager file. It ensures that each user can belong to only one group, similar to a OneToOne relationship.


from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

def move_user_to_group(username , group_name):
    User = get_user_model() # User model
    user = User.objects.get(username=username)  # Fetch the user object
    group, _ = Group.objects.get_or_create(name=group_name)
    user.groups.set([group])  # Assign the group