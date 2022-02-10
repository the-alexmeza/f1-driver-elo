# Generated by Django 3.2.12 on 2022-02-10 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('circuitRef', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10)),
                ('alt', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('driverRef', models.CharField(max_length=30)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=3, null=True)),
                ('forename', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('elo', models.PositiveIntegerField(default=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('url', models.URLField(blank=True)),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.circuit')),
            ],
        ),
        migrations.CreateModel(
            name='RaceResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.race')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='drivers',
            field=models.ManyToManyField(blank=True, through='ranking.RaceResult', to='ranking.Driver'),
        ),
        migrations.CreateModel(
            name='EloDelta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startingElo', models.PositiveIntegerField()),
                ('endingElo', models.PositiveIntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.race')),
            ],
        ),
    ]
