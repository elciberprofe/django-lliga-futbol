# Generated by Django 5.2.1 on 2025-05-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lliga', '0002_alter_lliga_data_inici'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lliga',
            name='data_fi',
            field=models.DateField(null=True),
        ),
    ]
