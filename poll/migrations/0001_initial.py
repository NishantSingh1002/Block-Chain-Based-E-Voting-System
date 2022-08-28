

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=18)),
                ('party', models.CharField(max_length=100)),
                ('criminalRecords', models.BooleanField(default=False)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
