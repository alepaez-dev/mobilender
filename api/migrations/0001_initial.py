# Generated by Django 3.1.7 on 2021-06-25 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssociatedCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('references', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('type_client', models.CharField(choices=[('normal', 'Normal'), ('plate', 'Plate'), ('gold', 'Gold'), ('platinum', 'Platinum')], default='normal', max_length=10)),
                ('key', models.CharField(blank=True, max_length=50, null=True)),
                ('photography', models.ImageField(blank=True, null=True, upload_to='')),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='DistributionCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_stocked', models.DateField(blank=True, null=True)),
                ('is_urgent', models.BooleanField(default=False)),
                ('associated_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='api.associatedcompany')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='api.client')),
                ('distribution_center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='api.distributioncenter')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('references', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_details', to='api.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_details', to='api.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='api.sucursal'),
        ),
        migrations.CreateModel(
            name='ItemProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_providers', to='api.item')),
                ('provider', models.ManyToManyField(blank=True, null=True, related_name='items_providers', to='api.Provider')),
            ],
        ),
    ]
