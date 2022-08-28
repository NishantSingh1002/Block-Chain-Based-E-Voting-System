

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20200424_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='private_key',
            field=models.CharField(max_length=300),
        ),
    ]
