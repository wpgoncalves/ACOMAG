# Generated by Django 4.0.2 on 2022-04-11 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='POBoxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('block', models.IntegerField(blank=True, null=True, verbose_name='Bloco')),
                ('type', models.CharField(choices=[('Simples', 'Simples'), ('Dupla', 'Dupla')], default='Simples', max_length=7, verbose_name='Tipo')),
                ('pib', models.IntegerField(blank=True, null=True, verbose_name='PIB')),
                ('extra_key', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Verificar', 'Verificar')], default='Verificar', max_length=9, verbose_name='Chave Reserva')),
                ('active', models.BooleanField(default=True, verbose_name='Ativa')),
            ],
            options={
                'verbose_name': 'Caixa Postal',
                'verbose_name_plural': 'Caixas Postais',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_validity', models.DateField(verbose_name='Vigência')),
                ('end_validity', models.DateField(verbose_name='Vencimento')),
                ('rent_value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Valor')),
                ('warned_in', models.DateField(blank=True, null=True, verbose_name='Avisado em')),
                ('sealed_in', models.DateField(blank=True, null=True, verbose_name='Lacrado em')),
                ('expired', models.BooleanField(default=False, verbose_name='Expirado')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.customers', verbose_name='Cliente')),
                ('pobox_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='poboxes.poboxes', verbose_name='Caixa Postal')),
            ],
            options={
                'verbose_name': 'Aluguel',
                'verbose_name_plural': 'Aluguéis',
                'ordering': ['pobox_id'],
            },
        ),
        migrations.AddConstraint(
            model_name='poboxes',
            constraint=models.UniqueConstraint(fields=('number',), name='poboxes_number_constraints'),
        ),
    ]
