# Generated by Django 5.0.2 on 2024-02-19 14:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_checker', '0012_alter_hipaachecklistitem_item_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISO27001ChecklistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.TextField()),
                ('checklist_number', models.IntegerField(default=1, help_text='The importance of the item')),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'ISO27001 Checklist Items',
                'ordering': ['control_group', 'item_description'],
            },
        ),
        migrations.CreateModel(
            name='ISO27001ControlGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_group_name', models.CharField(max_length=255)),
                ('control_group_number', models.IntegerField()),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'ISO27001 Control Groups',
                'ordering': ['control_group_name'],
            },
        ),
        migrations.RenameField(
            model_name='hipaachecklistresponse',
            old_name='checked_at',
            new_name='response_at',
        ),
        migrations.RenameField(
            model_name='pcichecklistresponse',
            old_name='checked_at',
            new_name='response_at',
        ),
        migrations.CreateModel(
            name='ISO27001ChecklistResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_status', models.BooleanField(default=False)),
                ('response_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('checklist_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compliance_checker.iso27001checklistitem')),
                ('control_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='iso_responses', to='compliance_checker.iso27001controlgroup')),
            ],
            options={
                'verbose_name_plural': 'ISO27001 Checklist Responses',
                'ordering': ['checklist_item'],
            },
        ),
        migrations.AddField(
            model_name='iso27001checklistitem',
            name='control_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iso_items', to='compliance_checker.iso27001controlgroup'),
        ),
    ]