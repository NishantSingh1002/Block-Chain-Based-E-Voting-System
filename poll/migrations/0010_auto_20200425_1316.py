

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0009_auto_20200425_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='public_key_n',
            field=models.CharField(max_length=320),
        ),
    ]
