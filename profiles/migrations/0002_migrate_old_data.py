from django.db import migrations

def migrate_old_data(apps, schema_editor):
    """
    Custom migration function to fill the new 'profiles' table: profiles_profile from 'oc_lettings_site'.

    Args:
        apps (Apps): The historical version of the migration model state.
        schema_editor (SchemaEditor): The schema editor.

    Returns:
        None
    """
    # Retrieve models from the 'profiles' app
    Profile = apps.get_model('profiles', 'Profile')
    
    # Retrieve data from the old 'oc_lettings_site_profile' table
    old_profiles = apps.get_model('oc_lettings_site', 'Profile').objects.all()

    # Insert data into the new 'profiles_profile' table
    for old_profile in old_profiles:
        Profile.objects.create(
            # Map old profile fields to new profile fields
            id=old_profile.id,
            favorite_city=old_profile.favorite_city,
            user_id=old_profile.user_id
        )
   
def reverse_migrate_old_data(apps, schema_editor):
    """
    Custom migration function to reverse the data insertion in 'profiles_profile' table.

    Args:
        apps (Apps): The historical version of the migration model state.
        schema_editor (SchemaEditor): The schema editor.

    Returns:
        None
    """
    # Retrieve models from the 'profiles' app
    Profile = apps.get_model('profiles', 'Profile')

    # Delete all data from the new 'Profile' table
    Profile.objects.all().delete()

class Migration(migrations.Migration):
    """
    Database migration to create the 'profiles' tables: (profiles_profile) and fill it with data from 'oc_lettings_site'.
    """

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_old_data, reverse_code=reverse_migrate_old_data),
    ]