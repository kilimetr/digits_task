# Generated by Django 3.2.4 on 2021-07-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather_Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Country Weather',
                'verbose_name_plural': 'Countries Weather',
            },
        ),
    ]