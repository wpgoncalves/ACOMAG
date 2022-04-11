# Generated by Django 4.0.2 on 2022-04-11 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holders',
            fields=[
                ('description', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Descrição')),
                ('operator', models.CharField(blank=True, max_length=255, null=True, verbose_name='Operador')),
                ('registration', models.CharField(blank=True, max_length=8, null=True, verbose_name='Matrícula')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('discontinued', models.BooleanField(default=False, verbose_name='Descontinuado')),
            ],
            options={
                'verbose_name': 'Detentor',
                'verbose_name_plural': 'Detentores',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('code', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True, verbose_name='Código')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('supply_branch', models.CharField(choices=[('Etiqueta', 'Etiqueta'), ('Insumos de Informática', 'Insumos de Informática'), ('Material de Consumo', 'Material de Consumo'), ('Produto', 'Produto'), ('Selo', 'Selo'), ('Terceiros', 'Terceiros'), ('Uniforme', 'Uniforme')], max_length=22, verbose_name='Ramo de Fornecimento')),
                ('group', models.CharField(choices=[('Aerogramas', 'Aerogramas'), ('Cadernos', 'Cadernos'), ('Caixas', 'Caixas'), ('Camisetas', 'Camisetas'), ('Cartões', 'Cartões'), ('Envelopes', 'Envelopes'), ('Etiquetas', 'Etiquetas'), ('Materiais', 'Materiais'), ('Selos', 'Selos'), ('Terceiros', 'Terceiros')], max_length=10, verbose_name='Grupo')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('to_supply', models.BooleanField(default=True, verbose_name='Suprir')),
                ('unit', models.CharField(choices=[('Unidade', 'Unidade'), ('Saco', 'Saco'), ('Bobina', 'Bobina'), ('Rolo', 'Rolo'), ('Caixa', 'Caixa'), ('Quilograma', 'Quilograma'), ('Frasco', 'Frasco'), ('Cartucho', 'Cartucho'), ('Resma', 'Resma'), ('Pacote', 'Pacote'), ('Bloco', 'Bloco'), ('Folha', 'Folha')], max_length=10, verbose_name='Unidade de medida')),
                ('quantity_unit', models.PositiveSmallIntegerField(verbose_name='Qtde por unidade')),
                ('min_quantity_supply', models.PositiveSmallIntegerField(verbose_name='Qtde mínima para suprimento')),
                ('discontinued', models.BooleanField(default=False, verbose_name='Descontinuado')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.SmallIntegerField(verbose_name='Qtde')),
                ('updated', models.DateField(auto_now=True, verbose_name='Atualizado em')),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.holders', verbose_name='Detentor')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.items', verbose_name='Item')),
            ],
            options={
                'verbose_name': 'Estoque',
                'verbose_name_plural': 'Estoque',
                'ordering': ['item'],
            },
        ),
    ]