# Generated by Django 3.0 on 2023-11-02 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_delete_models'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='Profile',
                    table='profiles_profile'
                )
                ],
        )
    ]
