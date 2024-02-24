# Generated by Django 4.1.1 on 2024-02-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rentApproval', '0006_renterproduct_approved_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renterproduct',
            name='is_approved',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('disapproved', 'Disapproved')], default='pending', max_length=20),
        ),
    ]