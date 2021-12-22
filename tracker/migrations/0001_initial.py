# Generated by Django 3.2.4 on 2021-12-22 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_date_time', models.DateTimeField()),
                ('is_approve', models.BooleanField(default=False)),
                ('is_reject', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('contact_no', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=150)),
                ('morning', models.BooleanField(default=False)),
                ('day', models.BooleanField(default=False)),
                ('night', models.BooleanField(default=False)),
                ('after_milk', models.BooleanField(default=False)),
                ('no_of_days', models.IntegerField()),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('contact_no', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('specialist', models.CharField(blank=True, max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.department'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.patient'),
        ),
    ]
