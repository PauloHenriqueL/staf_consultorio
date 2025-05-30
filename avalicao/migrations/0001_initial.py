# Generated by Django 5.2 on 2025-05-14 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliado',
            fields=[
                ('pk_avaliado', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome completo')),
                ('is_associate', models.BooleanField(default=False, verbose_name='É associado?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Avaliado',
                'verbose_name_plural': 'Avaliados',
            },
        ),
        migrations.CreateModel(
            name='Avaliador',
            fields=[
                ('pk_avaliador', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Avaliador',
                'verbose_name_plural': 'Avaliadores',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('pk_avaliacao', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_avaliacao', models.DateField(verbose_name='Data da Avalicao')),
                ('estagio_mudanca', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Estágio de Mudança')),
                ('estrutura', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Estruturação da Sessão')),
                ('encerramento', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Qualidade do Encerramento')),
                ('acolhimento', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Nível de Acolhimento')),
                ('seguranca_terapeuta', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Segurança Transmitida pelo Terapeuta')),
                ('seguranca_metodo', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Segurança no Método Aplicado')),
                ('aprofundar', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Capacidade de Aprofundamento')),
                ('hipoteses', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Formulação de Hipóteses')),
                ('interpretativa', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Capacidade Interpretativa')),
                ('frase_timing', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Timing e Qualidade das Frases')),
                ('corpo_setting', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Atenção ao Corpo e Setting')),
                ('insight_potencia', models.IntegerField(choices=[(-9, '-9'), (-3, '-3'), (-1, '-1'), (0, '0'), (1, '+1'), (3, '+3'), (9, '+9')], verbose_name='Potência de Insights Gerados')),
                ('fk_avaliado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Availicaos', to='avalicao.avaliado')),
                ('fk_avaliador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Availicaos', to='avalicao.avaliador')),
            ],
            options={
                'verbose_name': 'Availição',
                'verbose_name_plural': 'Availicões',
                'ordering': ['-dat_avaliacao'],
            },
        ),
    ]
