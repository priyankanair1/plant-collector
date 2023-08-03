# Generated by Django 3.2.20 on 2023-08-03 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_required', models.CharField(choices=[('I', 'Infrequent'), ('R', 'Regular'), ('F', 'Frequent')], default='I', max_length=1, verbose_name='watering required')),
            ],
        ),
    ]