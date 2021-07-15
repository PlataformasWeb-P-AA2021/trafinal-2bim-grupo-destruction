# Generated by Django 3.2.4 on 2021-07-11 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0003_auto_20210624_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_propietario', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=100)),
                ('num_cuartos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('residencial', 'Residencial'), ('rurall', 'Rural')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='numerotelefonico',
            name='estudiante',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='NumeroTelefonico',
        ),
        migrations.AddField(
            model_name='departamento',
            name='edificio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='administrativo.edificio'),
        ),
    ]