# Generated by Django 4.1.1 on 2024-02-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rentApproval', '0005_renterproduct_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='renterproduct',
            name='approved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
