# Generated by Django 4.0.5 on 2022-07-01 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regex', '0002_programao_programap_delete_teste'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosTm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha', models.IntegerField(max_length=8)),
                ('variavel_o', models.CharField(max_length=50)),
                ('variavel_p', models.CharField(max_length=50)),
                ('codigo_linha', models.CharField(max_length=1000)),
            ],
        ),
    ]
