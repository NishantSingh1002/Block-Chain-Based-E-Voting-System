

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0007_auto_20200425_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='private_key_e',
            new_name='public_key_e',
        ),
        migrations.RenameField(
            model_name='voter',
            old_name='private_key_n',
            new_name='public_key_n',
        ),
    ]
