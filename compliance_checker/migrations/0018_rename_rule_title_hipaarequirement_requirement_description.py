# Generated by Django 5.0.2 on 2024-02-19 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_checker', '0017_alter_pcichecklistresponse_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hipaarequirement',
            old_name='rule_title',
            new_name='requirement_description',
        ),
    ]
