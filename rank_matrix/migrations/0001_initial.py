# Generated by Django 3.2.7 on 2023-02-19 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigIntegerField()),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=255)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.CharField(blank=True, max_length=255, null=True)),
                ('branch_code', models.CharField(blank=True, max_length=255, null=True)),
                ('data_updated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='College_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigIntegerField()),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('display_code', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('nirf_3', models.BigIntegerField(default=10000)),
                ('nirf_2', models.BigIntegerField(default=10000)),
                ('nirf_1', models.BigIntegerField(default=10000)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('fax', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('current', models.CharField(blank=True, choices=[('Y', 'Currently Present'), ('N', 'Currently Not Present')], max_length=25, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('college_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.college_type')),
            ],
        ),
        migrations.CreateModel(
            name='Seat_Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_pool', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('seats', models.IntegerField(blank=True, null=True)),
                ('seats_change', models.BooleanField(default=False)),
                ('data_updated', models.BooleanField(default=False)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('category', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.category')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
                ('seat_pool', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.seat_pool')),
            ],
        ),
        migrations.CreateModel(
            name='Round7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('opening_rank', models.IntegerField(blank=True, null=True)),
                ('closing_rank', models.IntegerField(blank=True, null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('category', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.category')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
                ('seat_pool', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.seat_pool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('opening_rank', models.IntegerField(blank=True, null=True)),
                ('closing_rank', models.IntegerField(blank=True, null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('category', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.category')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
                ('seat_pool', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.seat_pool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('opening_rank', models.IntegerField(blank=True, null=True)),
                ('closing_rank', models.IntegerField(blank=True, null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('category', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.category')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
                ('seat_pool', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.seat_pool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('opening_rank', models.IntegerField(blank=True, null=True)),
                ('closing_rank', models.IntegerField(blank=True, null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('category', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.category')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
                ('seat_pool', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.seat_pool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('opening_rank', models.IntegerField(blank=True, null=True)),
                ('closing_rank', models.IntegerField(blank=True, null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('category', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.category')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
                ('seat_pool', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.seat_pool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('opening_rank', models.IntegerField(blank=True, null=True)),
                ('closing_rank', models.IntegerField(blank=True, null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('category', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.category')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
                ('seat_pool', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.seat_pool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('opening_rank', models.IntegerField(blank=True, null=True)),
                ('closing_rank', models.IntegerField(blank=True, null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('category', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.category')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
                ('seat_pool', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.seat_pool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='College_Quota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.CharField(max_length=5)),
                ('data_updated', models.BooleanField(default=False)),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
            ],
        ),
        migrations.CreateModel(
            name='College_Branch',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('current', models.CharField(blank=True, max_length=5, null=True)),
                ('data_updated', models.BooleanField(default=False)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.branch')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_matrix.institute')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='currently_present',
            field=models.ManyToManyField(blank=True, related_name='Currently_Present', to='rank_matrix.College_Type'),
        ),
        migrations.AddField(
            model_name='branch',
            name='previously_present',
            field=models.ManyToManyField(blank=True, related_name='Previously_Present', to='rank_matrix.College_Type'),
        ),
    ]
