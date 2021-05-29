# Generated by Django 3.2.2 on 2021-05-29 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('water_req', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='이름')),
                ('water_origin', models.CharField(max_length=32, verbose_name='취수원')),
                ('fe_origin', models.FloatField(verbose_name='철_취수원')),
                ('turbidity', models.FloatField(verbose_name='탁도')),
                ('date', models.IntegerField(verbose_name='일자')),
                ('fe_user', models.FloatField(verbose_name='철')),
                ('mn_user', models.FloatField(verbose_name='망간')),
                ('al_user', models.FloatField(verbose_name='알루미늄')),
                ('img', models.ImageField(upload_to='', verbose_name='육안검사')),
                ('total', models.CharField(max_length=32, verbose_name='종합평가')),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.member')),
                ('request_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='water_req.analysisrequest')),
            ],
            options={
                'verbose_name': '분석 결과',
                'verbose_name_plural': '분석 결과',
                'db_table': 'AnalysisData',
            },
        ),
    ]