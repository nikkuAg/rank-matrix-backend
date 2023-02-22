# Generated by Django 3.2.7 on 2023-02-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank_matrix', '0002_institute_available_branches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute',
            name='available_branches',
        ),
        migrations.AddField(
            model_name='institute',
            name='presently_available_branches',
            field=models.ManyToManyField(blank=True, default=None, related_name='Presently_Available_Branch', to='rank_matrix.Branch'),
        ),
        migrations.AddField(
            model_name='institute',
            name='previously_available_branches',
            field=models.ManyToManyField(blank=True, default=None, related_name='Previously_Available_Branch', to='rank_matrix.Branch'),
        ),
    ]