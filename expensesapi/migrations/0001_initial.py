# Generated by Django 4.0 on 2021-12-31 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ONLINE_SERVICES', 'ONLINE_SERVICES'), ('TRAVEL', 'TRAVEL'), ('FOOD', 'FOOD'), ('OTHERS', 'OTHERS')], max_length=200)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('description', models.TextField(max_length=350)),
                ('date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]
