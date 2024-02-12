# Generated by Django 5.0.1 on 2024-02-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_paymentmodel_delete_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmodel',
            name='m_timestamp',
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='m_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='m_payment_method',
            field=models.CharField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='paymentmodel',
            name='m_order_id',
            field=models.CharField(max_length=50),
        ),
    ]
