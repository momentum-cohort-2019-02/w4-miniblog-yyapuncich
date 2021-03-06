# Generated by Django 2.1.7 on 2019-03-10 01:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190309_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular comment across site.', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Title for your comments', max_length=100)),
                ('date_posted', models.DateTimeField(auto_now=True, verbose_name='commented on')),
                ('comment', models.TextField(help_text='Enter your lovely things to say!', max_length=200)),
                ('blog_entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.BlogPost')),
            ],
            options={
                'ordering': ['date_posted'],
            },
        ),
    ]
