# Generated by Django 4.0.4 on 2022-05-12 12:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_uuidbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUIDCategory',
            fields=[
                ('catid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='LegacyBook',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.book',),
        ),
        migrations.AlterField(
            model_name='uuidbook',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='uuidbook',
            name='categories',
            field=models.ManyToManyField(blank=True, to='core.uuidcategory'),
        ),
    ]