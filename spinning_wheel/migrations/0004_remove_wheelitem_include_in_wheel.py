# Generated by Django 5.0.1 on 2024-02-03 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spinning_wheel', '0003_remove_wheelitem_is_chosen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wheelitem',
            name='include_in_wheel',
        ),
    ]
