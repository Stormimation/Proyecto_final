# Generated by Django 3.1.7 on 2021-11-20 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_delete_usuariop2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Agendar',
            fields=[
                ('idHora', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.dia')),
                ('hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.hora')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.medico')),
                ('mes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.mes')),
            ],
        ),
    ]
