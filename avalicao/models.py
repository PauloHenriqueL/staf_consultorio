# avaliacao/models.py
from django.db import models
from django.contrib.auth.models import User  # Importe o modelo User


class Avaliador(models.Model):
    pk_avaliador = models.AutoField(primary_key=True, verbose_name='ID')
    nome = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Avaliador'
        verbose_name_plural = 'Avaliadores'

class Avaliado(models.Model):
    pk_avaliado = models.AutoField(primary_key=True, verbose_name='ID')
    nome = models.CharField(max_length=200, verbose_name='Nome completo')
    is_associate = models.BooleanField(default=False, verbose_name='É associado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Avaliado'
        verbose_name_plural = 'Avaliados'


class Avaliacao(models.Model):
    pk_avaliacao = models.AutoField(primary_key=True, verbose_name='ID')
    fk_avaliador = models.ForeignKey(Avaliador, on_delete=models.CASCADE, related_name='Availicaos')
    fk_avaliado = models.ForeignKey(Avaliado, on_delete=models.CASCADE, related_name='Availicaos')
    dat_avaliacao  = models.DateField(verbose_name="Data da Avalicao")

    SCORE_CHOICES = [
        (-9, '-9'),
        (-3, '-3'),
        (-1, '-1'),
        (0, '0'),
        (1, '+1'),
        (3, '+3'),      
        (9, '+9'),
    ]

    estagio_mudanca = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Estágio de Mudança")
    estrutura = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Estruturação da Sessão")
    encerramento = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Qualidade do Encerramento")
    acolhimento = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Nível de Acolhimento")
    seguranca_terapeuta = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Segurança Transmitida pelo Terapeuta")
    seguranca_metodo = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Segurança no Método Aplicado")
    aprofundar = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Capacidade de Aprofundamento")
    hipoteses = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Formulação de Hipóteses")
    interpretativa = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Capacidade Interpretativa")
    frase_timing = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Timing e Qualidade das Frases")
    corpo_setting = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Atenção ao Corpo e Setting")
    insight_potencia = models.IntegerField(choices=SCORE_CHOICES, verbose_name="Potência de Insights Gerados")
    
    def __str__(self):
        return f"Availição do {self.fk_avaliado} pelo {self.fk_avaliador}"
    
    class Meta:
        verbose_name = 'Availiallos'
        verbose_name_plural = 'Availiallos'
        ordering = ['-dat_avaliacao']  # Most recent first