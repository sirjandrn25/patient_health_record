# Generated by Django 3.2.4 on 2021-12-22 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_labreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='appointment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tracker.appointment'),
        ),
    ]
