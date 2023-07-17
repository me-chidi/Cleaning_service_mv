# Generated by Django 4.2.2 on 2023-07-06 15
from django.db import migrations, models

def update_duplicate_usernames(apps, schema_editor):
    Customer = apps.get_model('main', 'Customer')
    duplicates = Customer.objects.values('username').annotate(count=models.Count('username')).filter(count__gt=1)
    for duplicate in duplicates:
        username = duplicate['username']
        # Modify the username to make it unique, e.g., by appending a number
        new_username = f'{username}_1'
        Customer.objects.filter(username=username).update(username=new_username)

class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_alter_customer_managers_alter_customer_groups_and_more"),
    ]


    operations = [
        migrations.RunPython(update_duplicate_usernames),
    ]