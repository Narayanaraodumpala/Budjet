# Generated by Django 3.0 on 2020-12-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budjetapp', '0005_consults_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consults',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
