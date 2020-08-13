# Generated by Django 3.0 on 2020-08-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200813_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]