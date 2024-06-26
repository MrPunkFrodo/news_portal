from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluationAuthor', models.SmallIntegerField(default=0.0)),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_post', models.CharField(max_length=128)),
                ('text_post', models.TextField()),
                ('rating', models.SmallIntegerField(default=0.0)),
                ('content_type', models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2)),
                ('date_post', models.DateTimeField(auto_now_add=True)),
                ('postCategory', models.ManyToManyField(through='news.PostCategory', to='news.category')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.authors')),
            ],
        ),
        migrations.AddField(
            model_name='postcategory',
            name='categoryThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.posts'),
        ),
        migrations.AddField(
            model_name='postcategory',
            name='postThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField()),
                ('date_comment', models.DateTimeField(auto_now_add=True)),
                ('rating', models.SmallIntegerField(default=0.0)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.posts')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]