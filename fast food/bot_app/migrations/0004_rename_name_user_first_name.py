# Generated by Django 4.1.4 on 2023-02-09 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_app', '0003_alter_user_chat_id_alter_user_lang_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
    ]