# Generated by Django 3.2.9 on 2021-12-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='exerciseneeds',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='friendliness',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='sheddingamount',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='size',
            field=models.CharField(choices=[('TN', 'Tiny'), ('SM', 'Small'), ('MD', 'Medium'), ('LR', 'Large')], default='MD', max_length=100),
        ),
        migrations.AlterField(
            model_name='breed',
            name='trainability',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
    ]
