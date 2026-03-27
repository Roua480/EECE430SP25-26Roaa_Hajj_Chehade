from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoleyPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateJoined', models.DateField()),
                ('position', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contactPerson', models.CharField(max_length=100)),
            ],
        ),
    ]
