# Generated by Django 2.1.7 on 2019-03-09 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name as you would like it displayed.', max_length=50)),
                ('profile_pic', models.ImageField(upload_to='', verbose_name='Photo')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title for your post.', max_length=50)),
                ('blog_entry', models.TextField(verbose_name='Thoughts!')),
                ('blogger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Blogger')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the topic for your blog post', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topic',
            field=models.ManyToManyField(help_text='Select a topic.', to='core.Topic'),
        ),
    ]
