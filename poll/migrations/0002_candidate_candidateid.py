

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='candidateID',
            field=models.IntegerField(db_index=True, default=-1),
            preserve_default=False,
        ),
    ]
