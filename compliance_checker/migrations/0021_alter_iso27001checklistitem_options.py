# Generated by Django 5.0.2 on 2024-02-19 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_checker', '0020_alter_iso27001checklistitem_control_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iso27001checklistitem',
            options={'ordering': ['control_group', 'checklist_number'], 'verbose_name_plural': 'ISO27001 Checklist Items'},
        ),
    ]
