# Generated by Django 3.0.5 on 2020-04-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead0',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='head0',
            new_name='head',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head2',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
