from customers.models import Customers
from django.db import models


class POBoxes(models.Model):

    class TypeChoices(models.TextChoices):
        SIMPLES = 'Simples', 'Simples'
        DUPLA = 'Dupla', 'Dupla'

    class ExtraKeyChoices(models.TextChoices):
        SIM = 'Sim', 'Sim'
        NAO = 'Não', 'Não'
        VERIFICAR = 'Verificar', 'Verificar'

    number = models.IntegerField(verbose_name='Número')

    block = models.IntegerField(verbose_name='Bloco',
                                blank=True,
                                null=True)

    type = models.CharField(max_length=7,
                            verbose_name='Tipo',
                            choices=TypeChoices.choices,
                            default='Simples')

    pib = models.IntegerField(verbose_name='PIB',
                              blank=True,
                              null=True)

    extra_key = models.CharField(max_length=9,
                                 verbose_name='Chave Reserva',
                                 choices=ExtraKeyChoices.choices,
                                 default='Verificar')

    active = models.BooleanField(verbose_name='Ativa',
                                 default=True)

    class Meta:
        ordering = ['number']
        verbose_name = 'Caixa Postal'
        verbose_name_plural = 'Caixas Postais'
        constraints = [
            models.UniqueConstraint(
                fields=['number', ],
                name='poboxes_number_constraints'
            )
        ]

    def __str__(self):
        return str(self.number)


class Rentals(models.Model):

    pobox_id = models.OneToOneField(POBoxes,
                                    on_delete=models.PROTECT,
                                    verbose_name='Caixa Postal')

    customer_id = models.ForeignKey(Customers,
                                    on_delete=models.PROTECT,
                                    verbose_name='Cliente')

    start_validity = models.DateField(verbose_name='Vigência')

    end_validity = models.DateField(verbose_name='Vencimento')

    rent_value = models.DecimalField(max_digits=6,
                                     decimal_places=2,
                                     verbose_name='Valor',
                                     blank=True,
                                     null=True)

    warned_in = models.DateField(verbose_name='Avisado em',
                                 blank=True,
                                 null=True)

    sealed_in = models.DateField(verbose_name='Lacrado em',
                                 blank=True,
                                 null=True)

    expired = models.BooleanField(default=False,
                                  verbose_name='Expirado')

    class Meta:
        ordering = ['pobox_id']
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Aluguéis'

    def __str__(self):
        return str(self.pobox_id)
