# Generated by Django 4.0.4 on 2022-05-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
