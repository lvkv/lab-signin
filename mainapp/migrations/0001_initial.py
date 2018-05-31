# Generated by Django 2.0.5 on 2018-05-31 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('paggarwal', 'Priya Aggarwal'), ('sbudhan', 'Stephanie Budhan'), ('wchiang', 'Woody Chiang'), ('dkwasniak', 'Dominika Kwasniak'), ('kledalla', 'Karthik Ledalla'), ('mlee', 'Matthew Lee'), ('nlo', 'Natalie Lo'), ('mmullin', 'Matthew Mullin'), ('lypan', 'Lin Yu Pan'), ('jrakhimov', 'Jennifer Rakhimov'), ('rruzic', 'Robert Ruzic'), ('mshah', 'Manvi Shah'), ('lvelikov', 'Lukas Velikov'), ('svincent', 'Sara Vincent')], max_length=9)),
                ('sign_in_time', models.DateTimeField()),
                ('sign_out_time', models.DateTimeField()),
                ('total_time', models.TimeField()),
            ],
        ),
    ]
