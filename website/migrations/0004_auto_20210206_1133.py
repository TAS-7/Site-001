# Generated by Django 3.1.2 on 2021-02-06 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='approved_answer',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='date_posted',
        ),
    ]