

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_auto_20200424_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='private_key',
        ),
        migrations.AddField(
            model_name='voter',
            name='private_key_e',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='voter',
            name='private_key_n',
            field=models.IntegerField(default=0),
        ),
    ]
