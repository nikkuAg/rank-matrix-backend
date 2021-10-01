# Generated by Django 3.2.6 on 2021-09-28 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20210912_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branches',
            old_name='name',
            new_name='branch_name',
        ),
        migrations.RemoveField(
            model_name='institutes',
            name='quota',
        ),
        migrations.AddField(
            model_name='branches',
            name='degree',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='branches',
            name='duration',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='round1_2016',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2016',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2017',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2017',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2018',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2018',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2019',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2019',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2020',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round1_2020',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round2_2020',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round2_2020',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round3_2020',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round3_2020',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round4_2020',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round4_2020',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round5_2020',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round5_2020',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round6_2016',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round6_2016',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round6_2020',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round6_2020',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round7_2017',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round7_2017',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round7_2018',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round7_2018',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round7_2019',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round7_2019',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round_2015',
            name='quota',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='round_2015',
            name='seat_pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='round1_2016',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round1_2017',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round1_2018',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round1_2019',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round1_2020',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round2_2020',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round3_2020',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round4_2020',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round5_2020',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round6_2016',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round6_2020',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round7_2017',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round7_2018',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round7_2019',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='round_2015',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='SeatMatrix_2020_CSAB',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quota', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('seat_pool', models.CharField(max_length=100, null=True)),
                ('seats', models.IntegerField(null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.branches')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutes')),
            ],
        ),
        migrations.CreateModel(
            name='SeatMatrix_2020',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quota', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('seat_pool', models.CharField(max_length=100, null=True)),
                ('seats', models.IntegerField(null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.branches')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutes')),
            ],
        ),
        migrations.CreateModel(
            name='SeatMatrix_2019',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quota', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('seat_pool', models.CharField(max_length=100, null=True)),
                ('seats', models.IntegerField(null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.branches')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutes')),
            ],
        ),
        migrations.CreateModel(
            name='Provisional_2020',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quota', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('seat_pool', models.CharField(max_length=100, null=True)),
                ('opening_rank', models.IntegerField(null=True)),
                ('closing_rank', models.IntegerField(null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.branches')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutes')),
            ],
        ),
        migrations.CreateModel(
            name='Provisional_2019',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quota', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('seat_pool', models.CharField(max_length=100, null=True)),
                ('opening_rank', models.IntegerField(null=True)),
                ('closing_rank', models.IntegerField(null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.branches')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutes')),
            ],
        ),
        migrations.CreateModel(
            name='Provisional_2018',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quota', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('seat_pool', models.CharField(max_length=100, null=True)),
                ('opening_rank', models.IntegerField(null=True)),
                ('closing_rank', models.IntegerField(null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.branches')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutes')),
            ],
        ),
        migrations.CreateModel(
            name='CSAB_2020',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quota', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('seat_pool', models.CharField(max_length=100, null=True)),
                ('opening_rank', models.IntegerField(null=True)),
                ('closing_rank', models.IntegerField(null=True)),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.branches')),
                ('institute_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutes')),
            ],
        ),
    ]