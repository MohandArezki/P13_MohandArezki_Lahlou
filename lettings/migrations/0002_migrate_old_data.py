from django.db import migrations

def migrate_old_data(apps, schema_editor):
    """
    Custom migration function to fill the new 'lettings' tables: (lettings_address, lettings_letting) from 'oc_lettings_site'.

    Args:
        apps (Apps): The historical version of the migration model state.
        schema_editor (SchemaEditor): The schema editor.

    Returns:
        None
    """
    LettingsAddress = apps.get_model('lettings', 'Address')
    LettingsLetting = apps.get_model('lettings', 'Letting')
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')

    # Retrieve data from the old 'oc_lettings_site_address' table
    old_addresses = OldAddress.objects.all()

    # Insert data into the new 'lettings_address' table
    for old_address in old_addresses:
        LettingsAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )

    # Retrieve data from the old 'oc_lettings_site_letting' table
    old_lettings = OldLetting.objects.all()

    # Insert data into the new 'lettings_letting' table
    for old_letting in old_lettings:
        # Retrieve the corresponding address for the old letting
        old_address = old_letting.address

        # Create a new LettingsLetting instance and associate it with the LettingsAddress instance
        LettingsLetting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address=LettingsAddress.objects.get(
                number=old_address.number,
                street=old_address.street,
                city=old_address.city,
                state=old_address.state,
                zip_code=old_address.zip_code,
                country_iso_code=old_address.country_iso_code
            )
        )

def reverse_migrate_old_data(apps, schema_editor):
    """
    Custom migration function to reverse the data insertion in 'lettings_address' and 'lettings_letting' tables.

    Args:
        apps (Apps): The historical version of the migration model state.
        schema_editor (SchemaEditor): The schema editor.

    Returns:
        None
    """
    LettingsAddress = apps.get_model('lettings', 'Address')
    LettingsLetting = apps.get_model('lettings', 'Letting')

    # Delete all data from the new 'LettingsAddress' table
    LettingsAddress.objects.all().delete()

    # Delete all data from the new 'LettingsLetting' table
    LettingsLetting.objects.all().delete()

class Migration(migrations.Migration):
    """
    Database migration to create the 'lettings' tables: (lettings_address, lettings_letting) and fill them with data from 'oc_lettings_site'.
    """

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_old_data, reverse_code=reverse_migrate_old_data),
    ]
