# role_based_access_controls.py
from django.contrib.auth.models import Group, Permission
from management_apps.models import CustomUser

# Create a group for customers
customer_group, created = Group.objects.get_or_create(name='Customer')

# Assign permissions to the customer group
customer_permissions = ['add_booking', 'view_booking', 'add_testimonial']
for perm in customer_permissions:
    permission = Permission.objects.get(codename=perm)
    customer_group.permissions.add(permission)

# Add a user to the customer group
user = CustomUser.objects.get(username='john_doe')
user.groups.add(customer_group)

print(f"User '{user.username}' has been added to the group '{customer_group.name}'.")
