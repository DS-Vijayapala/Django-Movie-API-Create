# Generated by Django 5.1.7 on 2025-03-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(choices=[('action', 'action'), ('cartoon', 'cartoon')], max_length=20),
        ),
    ]
