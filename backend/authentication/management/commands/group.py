from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model



"""
Usage:
  python manage.py group --add <GROUP_NAME>
      → Creates a new group with the given name (if it doesn’t already exist).

  python manage.py group --delete <GROUP_NAME>
      → Deletes the group with the given name (if it exists).

  python manage.py group --list <GROUP_NAME>
      → Lists all users that belong to the given group.

  python manage.py group --username <USERNAME> --group <GROUP_NAME>
      → Adds a user to a group.

  python manage.py group --username <USERNAME> --group <GROUP_NAME> --removeuser
      → Removes a user from a group.

For more details, see COMMAND.md
"""


class Command(BaseCommand):
    """
    Management command for managing Django auth groups and user memberships.
    """

    help = "Add/delete groups, list users, and manage user memberships"

    def add_arguments(self, parser):
        parser.add_argument("--add", type=str, help="Name of the group to add")
        parser.add_argument("--delete", type=str, help="Name of the group to delete")
        parser.add_argument("--list", type=str, help="List all users in the given group")
        parser.add_argument("--username", type=str, help="Username of the user")
        parser.add_argument("--group", type=str, help="Name of the group to add/remove user")
        parser.add_argument("--removeuser", action="store_true", help="Remove user from group")

    def handle(self, *args, **options):
        add = options.get("add")
        delete = options.get("delete")
        ls = options.get("list")
        username = options.get("username")
        group_name = options.get("group")
        remove_user = options.get("removeuser")

        User = get_user_model()

        # Add a group
        if add:
            if Group.objects.filter(name=add).exists():
                self.stdout.write(self.style.WARNING(f"Group '{add}' already exists!"))
            else:
                Group.objects.create(name=add)
                self.stdout.write(self.style.SUCCESS(f"Group '{add}' added successfully!"))

        # Delete a group
        elif delete:
            if Group.objects.filter(name=delete).exists():
                Group.objects.get(name=delete).delete()
                self.stdout.write(self.style.SUCCESS(f"Group '{delete}' deleted successfully!"))
            else:
                self.stdout.write(self.style.ERROR(f"No group named '{delete}' exists!"))

        # List users in a group
        elif ls:
            group = Group.objects.filter(name=ls).first()
            if group:
                users_in_group = group.user_set.all()
                if users_in_group:
                    self.stdout.write(self.style.SUCCESS(f"Users in group '{ls}':"))
                    for user in users_in_group:
                        self.stdout.write(f"- {user.username} | {user.first_name or "null"}")
                else:
                    self.stdout.write(self.style.WARNING("No users in this group."))
            else:
                self.stdout.write(self.style.ERROR(f"No group named '{ls}' exists!"))

        # Add or remove user from a group
        elif username and group_name:
            try:
                user = User.objects.get(username=username)
                group = Group.objects.get(name=group_name)


                if remove_user:
                    if group in user.groups.all():
                        user.groups.remove(group)
                        self.stdout.write(self.style.SUCCESS(
                            f"User '{username}' removed from group '{group_name}' successfully!"
                        ))
                    else:
                        self.stdout.write(self.style.WARNING(
                            f"User '{username}' is not in group '{group_name}'."
                        ))
                else:
                    if group in user.groups.all():
                        self.stdout.write(self.style.WARNING(
                            f"User '{username}' is already in group '{group_name}'."
                        ))
                    else:
                        user.groups.add(group)
                        self.stdout.write(self.style.SUCCESS(
                            f"User '{username}' added to group '{group_name}' successfully!"
                        ))

            except Group.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"No group named '{group_name}' exists!"))
            except User.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"No user with username '{username}' exists!"))

        else:
            self.stdout.write(self.style.WARNING(
                "Invalid arguments. Run `python manage.py group --help` for usage information."
            ))
