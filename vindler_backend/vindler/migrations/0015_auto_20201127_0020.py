# Generated by Django 3.1.3 on 2020-11-26 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vindler', '0014_auto_20201126_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vindles',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vindles', to=settings.AUTH_USER_MODEL),
        ),
    ]
