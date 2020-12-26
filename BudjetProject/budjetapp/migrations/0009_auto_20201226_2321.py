# Generated by Django 3.0 on 2020-12-26 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budjetapp', '0008_graphs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphs',
            old_name='name',
            new_name='status',
        ),
        migrations.AddField(
            model_name='graphs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]