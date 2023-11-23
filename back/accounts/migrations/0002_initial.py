# Generated by Django 4.2.7 on 2023-11-23 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propensity',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bank'),
        ),
        migrations.AddField(
            model_name='propensity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
