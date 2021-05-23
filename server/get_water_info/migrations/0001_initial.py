# Generated by Django 3.2.2 on 2021-05-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='이름')),
                ('phone', models.CharField(max_length=32, verbose_name='연락처')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
            ],
            options={
                'verbose_name': '분석 결과',
                'verbose_name_plural': '분석 결과',
                'db_table': 'AnalysisData',
            },
        ),
    ]
