# Generated by Django 5.0 on 2023-12-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hello_app', '0005_delete_stdreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
                ('Password', models.CharField(max_length=12)),
                ('PhoneNumber', models.CharField(max_length=20)),
                ('YearofCollege', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
    ]
