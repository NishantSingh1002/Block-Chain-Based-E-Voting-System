

from django.db import migrations, models
import poll.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0010_auto_20200425_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('vote', models.IntegerField(default=0)),
                ('timestamp', models.FloatField(default=poll.models.get_time)),
                ('block_id', models.IntegerField(null=True)),
            ],
        ),
    ]
