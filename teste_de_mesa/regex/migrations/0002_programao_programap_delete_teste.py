# Generated by Django 4.0.5 on 2022-07-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramaO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_codificacao', models.DateField()),
                ('codigo_o', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramaP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_codificacao', models.DateField()),
                ('codigo_p', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Teste',
        ),
    ]
