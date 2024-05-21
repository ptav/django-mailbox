# Generated by Django 3.2.23 on 2023-12-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0008_auto_20190219_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='eml',
            field=models.FileField(blank=True, help_text='Original full content of message', null=True, upload_to='messages', verbose_name='Raw message contents'),
        ),
    ]