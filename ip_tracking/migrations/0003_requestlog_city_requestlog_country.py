# Generated by Django 4.2.23 on 2025-07-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_tracking', '0002_blockedip'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlog',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requestlog',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
