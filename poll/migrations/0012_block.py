

from django.db import migrations, models
import poll.models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0011_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_hash', models.CharField(blank=True, max_length=64)),
                ('merkle_hash', models.CharField(blank=True, max_length=64)),
                ('self_hash', models.CharField(blank=True, max_length=64)),
                ('nonce', models.IntegerField(null=True)),
                ('timestamp', models.FloatField(default=poll.models.get_time)),
            ],
        ),
    ]
