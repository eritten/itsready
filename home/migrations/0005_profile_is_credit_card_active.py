# Generated by Django 3.2 on 2023-11-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_creditcard_card_holder_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_credit_card_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
