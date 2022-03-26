# Generated by Django 4.0.2 on 2022-03-25 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('type', models.CharField(choices=[('Aeroporto', 'Aeroporto'), ('Alameda', 'Alameda'), ('Área', 'Área'), ('Avenida', 'Avenida'), ('Campo', 'Campo'), ('Chácara', 'Chácara'), ('Colônia', 'Colônia'), ('Condomínio', 'Condomínio'), ('Conjunto', 'Conjunto'), ('Distrito', 'Distrito'), ('Esplanada', 'Esplanada'), ('Estação', 'Estação'), ('Estrada', 'Estrada'), ('Favela', 'Favela'), ('Fazenda', 'Fazenda'), ('Feira', 'Feira'), ('Jardim', 'Jardim'), ('Ladeira', 'Ladeira'), ('Lago', 'Lago'), ('Lagoa', 'Lagoa'), ('Largo', 'Largo'), ('Loteamento', 'Loteamento'), ('Morro', 'Morro'), ('Núcleo', 'Núcleo'), ('Parque', 'Parque'), ('Passarela', 'Passarela'), ('Pátio', 'Pátio'), ('Praça', 'Praça'), ('Quadra', 'Quadra'), ('Recanto', 'Recanto'), ('Residencial', 'Residencial'), ('Rodovia', 'Rodovia'), ('Rua', 'Rua'), ('Setor', 'Setor'), ('Sítio', 'Sítio'), ('Travessa', 'Travessa'), ('Trecho', 'Trecho'), ('Trevo', 'Trevo'), ('Vale', 'Vale'), ('Vereda', 'Vereda'), ('Via', 'Via'), ('Viaduto', 'Viaduto'), ('Viela', 'Viela'), ('Vila', 'Vila')], max_length=60, verbose_name='Tipo')),
                ('address', models.CharField(max_length=255, verbose_name='Endereço')),
                ('district', models.CharField(max_length=120, verbose_name='Bairro')),
                ('city', models.CharField(max_length=120, verbose_name='Cidade')),
                ('state', models.CharField(choices=[('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal')], max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'ordering': ['cep'],
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('Física', 'Física'), ('Jurídica', 'Jurídica')], max_length=8, verbose_name='Tipo')),
                ('cpf_cnpj', models.CharField(max_length=14, verbose_name='CPF/CNPJ')),
                ('ie_rg', models.CharField(blank=True, max_length=12, verbose_name='IE/RG')),
                ('country', models.CharField(blank=True, max_length=60, verbose_name='País')),
                ('passport', models.CharField(blank=True, max_length=8, verbose_name='Passaporte')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('responsible', models.CharField(blank=True, max_length=100, verbose_name='Responsável')),
                ('address_number', models.IntegerField(verbose_name='Número')),
                ('address_complement', models.CharField(blank=True, max_length=120, verbose_name='Complemento')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11, verbose_name='Telefone')),
                ('type', models.CharField(choices=[('Residêncial', 'Residêncial'), ('Celular', 'Celular'), ('Comercial', 'Comercial')], max_length=11, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
                'ordering': ['number'],
            },
        ),
        migrations.AddConstraint(
            model_name='phones',
            constraint=models.UniqueConstraint(fields=('number',), name='phones_number_constraints'),
        ),
        migrations.AddConstraint(
            model_name='emails',
            constraint=models.UniqueConstraint(fields=('email',), name='emails_email_constraints'),
        ),
        migrations.AddField(
            model_name='customers',
            name='address',
            field=models.ManyToManyField(to='customers.Adresses', verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='customers',
            name='emails',
            field=models.ManyToManyField(blank=True, to='customers.Emails', verbose_name='E-mails'),
        ),
        migrations.AddField(
            model_name='customers',
            name='phones',
            field=models.ManyToManyField(blank=True, to='customers.Phones', verbose_name='Telefones'),
        ),
        migrations.AddConstraint(
            model_name='adresses',
            constraint=models.UniqueConstraint(fields=('cep',), name='adresses_cep_constraints'),
        ),
        migrations.AddConstraint(
            model_name='customers',
            constraint=models.UniqueConstraint(fields=('cpf_cnpj',), name='customers_cpf_cnpj_constraints'),
        ),
    ]
