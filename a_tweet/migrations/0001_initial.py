# Generated by Django 3.1.4 on 2021-03-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('no_tweets', models.PositiveIntegerField(default=100)),
                ('pos', models.FloatField(blank=True, null=True)),
                ('neg', models.FloatField(blank=True, null=True)),
                ('neutral', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
