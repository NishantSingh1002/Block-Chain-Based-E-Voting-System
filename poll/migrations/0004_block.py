

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20200423_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballot', models.CharField(max_length=200)),
                ('signature', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('error', models.BooleanField(default=False)),
            ],
        ),
    ]
