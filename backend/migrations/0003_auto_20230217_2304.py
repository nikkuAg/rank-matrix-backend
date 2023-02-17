# Generated by Django 3.2.7 on 2023-02-17 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_round2_round3_round4_round5_round6_round7'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Branches',
            new_name='Branch',
        ),
        migrations.RenameModel(
            old_name='Institutes',
            new_name='Institute',
        ),
        migrations.RenameModel(
            old_name='Updates',
            new_name='Update',
        ),
        migrations.RemoveField(
            model_name='college_quota',
            name='institute_code',
        ),
        migrations.DeleteModel(
            name='College_Branch',
        ),
        migrations.DeleteModel(
            name='College_Quota',
        ),
    ]
