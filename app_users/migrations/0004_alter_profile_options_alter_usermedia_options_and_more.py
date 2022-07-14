# Generated by Django 4.0.5 on 2022-07-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('change_active', 'Can change if user is active'),), 'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AlterModelOptions(
            name='usermedia',
            options={'permissions': (('change_verified', 'Can change if user media is verified'),), 'verbose_name': 'user_media', 'verbose_name_plural': 'user_medias'},
        ),
        migrations.AddField(
            model_name='usermedia',
            name='is_verified',
            field=models.BooleanField(default=True, verbose_name='is verified'),
        ),
    ]