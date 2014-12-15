# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contiene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id_Cuenta', models.AutoField(serialize=False, verbose_name=b'id_Cuenta', primary_key=True)),
                ('nombre_cuenta', models.TextField()),
                ('Seguidores', models.IntegerField()),
                ('Siguiendo', models.IntegerField()),
                ('numero_Tweets', models.IntegerField()),
                ('tipo_Cuenta', models.NullBooleanField()),
                ('Sexo', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id_Etiqueta', models.AutoField(serialize=False, verbose_name=b'id_Etiqueta', primary_key=True)),
                ('nombre_etiqueta', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id_Tweet', models.AutoField(serialize=False, verbose_name=b'id_Tweet', primary_key=True)),
                ('retweet', models.IntegerField()),
                ('favoritos', models.IntegerField()),
                ('tipo_Tweet', models.NullBooleanField()),
                ('texto', models.TextField()),
                ('fecha', models.DateField()),
                ('id_Cuenta', models.ForeignKey(to='pagina.Cuenta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contiene',
            name='id_Etiqueta',
            field=models.ForeignKey(to='pagina.Etiqueta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contiene',
            name='id_Tweet',
            field=models.ForeignKey(to='pagina.Tweet'),
            preserve_default=True,
        ),
    ]
