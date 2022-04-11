from django.db import models


class Holders(models.Model):

    description = models.CharField(max_length=20,
                                   verbose_name='Descrição',
                                   primary_key=True,
                                   unique=True)

    operator = models.CharField(max_length=255,
                                verbose_name='Operador',
                                blank=True,
                                null=True)

    registration = models.CharField(max_length=8,
                                    verbose_name='Matrícula',
                                    blank=True,
                                    null=True)

    comments = models.TextField(verbose_name='Observações',
                                blank=True,
                                null=True)

    discontinued = models.BooleanField(verbose_name='Descontinuado',
                                       default=False)

    class Meta:
        ordering = ['description']
        verbose_name = 'Detentor'
        verbose_name_plural = 'Detentores'

    def __str__(self):
        return self.description


class Items(models.Model):

    class GroupChoices(models.TextChoices):
        AEROGRAMS = 'Aerogramas', 'Aerogramas'
        NOTEBOOKS = 'Cadernos', 'Cadernos'
        BOXES = 'Caixas', 'Caixas'
        T_SHIRTS = 'Camisetas', 'Camisetas'
        CARDS = 'Cartões', 'Cartões'
        ENVELOPES = 'Envelopes', 'Envelopes'
        TAGS = 'Etiquetas', 'Etiquetas'
        MATERIALS = 'Materiais', 'Materiais'
        SEALS = 'Selos', 'Selos'
        THE_3RD = 'Terceiros', 'Terceiros'

    class SupplyBranchChoices(models.TextChoices):
        TAG = 'Etiqueta', 'Etiqueta'
        INPUTS = 'Insumos de Informática', 'Insumos de Informática'
        MATERIAL = 'Material de Consumo', 'Material de Consumo'
        PRODUCT = 'Produto', 'Produto'
        SEAL = 'Selo', 'Selo'
        THE_3RD = 'Terceiros', 'Terceiros'
        UNIFORM = 'Uniforme', 'Uniforme'

    class UnitChoices(models.TextChoices):
        UN = 'Unidade', 'Unidade'
        SC = 'Saco', 'Saco'
        BO = 'Bobina', 'Bobina'
        RO = 'Rolo', 'Rolo'
        CX = 'Caixa', 'Caixa'
        KG = 'Quilograma', 'Quilograma'
        FR = 'Frasco', 'Frasco'
        CH = 'Cartucho', 'Cartucho'
        RS = 'Resma', 'Resma'
        PA = 'Pacote', 'Pacote'
        BL = 'Bloco', 'Bloco'
        FL = 'Folha', 'Folha'

    code = models.CharField(max_length=9,
                            verbose_name='Código',
                            primary_key=True,
                            unique=True)

    description = models.CharField(max_length=255,
                                   verbose_name='Descrição')

    supply_branch = models.CharField(max_length=22,
                                     verbose_name='Ramo de Fornecimento',
                                     choices=SupplyBranchChoices.choices)

    group = models.CharField(max_length=10,
                             choices=GroupChoices.choices,
                             verbose_name='Grupo')

    value = models.DecimalField(verbose_name='Valor',
                                max_digits=8,
                                decimal_places=2)

    to_supply = models.BooleanField(verbose_name='Suprir',
                                    default=True)

    unit = models.CharField(max_length=10,
                            choices=UnitChoices.choices,
                            verbose_name='Unidade de medida')

    quantity_unit = models.PositiveSmallIntegerField(
        verbose_name='Qtde por unidade')

    min_quantity_supply = models.PositiveSmallIntegerField(
        verbose_name='Qtde mínima para suprimento')

    discontinued = models.BooleanField(verbose_name='Descontinuado',
                                       default=False)

    class Meta:
        ordering = ['description']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.description


class Stock(models.Model):

    item = models.ForeignKey(Items,
                             on_delete=models.PROTECT,
                             verbose_name='Item')

    amount = models.SmallIntegerField(verbose_name='Qtde')

    holder = models.ForeignKey(Holders,
                               on_delete=models.PROTECT,
                               verbose_name='Detentor')

    updated = models.DateField(auto_now=True,
                               verbose_name='Atualizado em')

    class Meta:
        ordering = ['item']
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'

    def __str__(self):
        return str(self.item)
