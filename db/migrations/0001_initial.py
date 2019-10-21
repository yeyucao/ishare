# Generated by Django 2.0.7 on 2019-10-18 18:47

import DjangoUeditor.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shortuuid.main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='作者昵称、2~30个字符', max_length=30, unique=True, verbose_name='username')),
                ('email', models.EmailField(help_text='作为登录账号，绑定后不可修改', max_length=254, unique=True, verbose_name='账号邮箱')),
                ('header', models.ImageField(blank=True, null=True, upload_to='header/', verbose_name='头像')),
                ('desc', models.TextField(blank=True, help_text='200字描述一下自己', max_length=200, null=True, verbose_name='简介')),
                ('alipay', models.ImageField(blank=True, null=True, upload_to='dsm/alipay/', verbose_name='支付宝打赏码')),
                ('wechat', models.ImageField(blank=True, null=True, upload_to='dsm/wechat/', verbose_name='微信打赏码')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '账户',
                'db_table': 'user_account',
                'verbose_name': '账户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(max_length=20, verbose_name='广告名')),
                ('image', models.ImageField(blank=True, upload_to='ad/', verbose_name='图片')),
                ('link', models.URLField(verbose_name='广告链接')),
                ('adtype', models.PositiveSmallIntegerField(blank=True, choices=[(0, '右侧方形广告'), (1, '左侧长条广告')], null=True, verbose_name='广告类型')),
                ('remark', models.TextField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('add', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='最近修改')),
                ('end', models.DateTimeField(null=True, verbose_name='结束时间')),
            ],
            options={
                'verbose_name_plural': '广告',
                'db_table': 'advertisement',
                'verbose_name': '广告',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(default=shortuuid.main.ShortUUID.random, max_length=12, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='1~32个字', max_length=32, verbose_name='标题')),
                ('cover', models.ImageField(blank=True, upload_to='blog/cover/', verbose_name='封面')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容')),
                ('source', models.URLField(blank=True, help_text='如果转载, 则提供原文链接', null=True, verbose_name='原文链接')),
                ('is_fine', models.BooleanField(default=False, verbose_name='站长推荐')),
                ('is_top', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('read', models.PositiveIntegerField(default=0, verbose_name='阅读数')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('add', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='最后修改')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('author', models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '博客',
                'db_table': 'blog',
                'verbose_name': '博客',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.CharField(default=shortuuid.main.ShortUUID.random, max_length=4, primary_key=True, serialize=False, verbose_name='专题id')),
                ('bname', models.CharField(max_length=32, unique=True, verbose_name='专题名称')),
                ('cat', models.CharField(choices=[('A', '文学创作'), ('B', '技术分享')], default='A', max_length=1, verbose_name='专题类别')),
                ('cover', models.ImageField(blank=True, upload_to='book/cover', verbose_name='专题封面')),
                ('desc', models.TextField(help_text='2~300文字', max_length=300, verbose_name='专题简介')),
                ('read', models.PositiveIntegerField(default=0, verbose_name='累计阅读')),
                ('add', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='最近修改')),
                ('is_fine', models.BooleanField(default=True, verbose_name='是否推荐')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可见')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '专题',
                'db_table': 'book',
                'verbose_name': '专题',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_cat', models.CharField(choices=[('A', '文学类'), ('B', '技术类')], max_length=1, verbose_name='前置分类')),
                ('cat', models.CharField(help_text='1~12个字', max_length=12, verbose_name='类别')),
                ('add', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='最近修改')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
            options={
                'verbose_name_plural': '类别',
                'db_table': 'category',
                'verbose_name': '类别',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.CharField(default=shortuuid.main.ShortUUID.random, max_length=6, primary_key=True, serialize=False, verbose_name='章节id')),
                ('title', models.CharField(max_length=32, verbose_name='章节标题')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容')),
                ('add', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='上次修改')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可见')),
                ('book', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='bchapters', to='db.Book', verbose_name='所属专题')),
            ],
            options={
                'verbose_name_plural': '章节',
                'db_table': 'chapter',
                'verbose_name': '章节',
            },
        ),
        migrations.CreateModel(
            name='Expand',
            fields=[
                ('key', models.CharField(help_text='1~16字符', max_length=16, primary_key=True, serialize=False, verbose_name='键')),
                ('value', models.CharField(help_text='1~32字符', max_length=32, verbose_name='值')),
                ('remark', models.TextField(max_length=100, null=True, verbose_name='备注')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='上次变更')),
            ],
            options={
                'verbose_name_plural': '拓展数据',
                'db_table': 'expand',
                'verbose_name': '拓展数据',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(help_text='完整的网站首页地址', max_length=64, unique=True, verbose_name='链接')),
                ('link_name', models.CharField(help_text='网站的名字', max_length=32, verbose_name='链接名称')),
                ('cat', models.PositiveSmallIntegerField(choices=[(0, '公益链接'), (1, '个人主页'), (2, '商业广告')], default=1, help_text='网站类型', verbose_name='链接类型')),
                ('email', models.EmailField(help_text='有特殊情况方便联系', max_length=32, verbose_name='邮箱')),
                ('add', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='最近修改')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否可用')),
            ],
            options={
                'verbose_name_plural': '友链',
                'db_table': 'link',
                'verbose_name': '友链',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='音乐名')),
                ('author', models.CharField(max_length=20, verbose_name='歌手')),
                ('code', models.TextField(max_length=300, verbose_name='外链代码')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='最后变更')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
            options={
                'verbose_name_plural': '外链音乐',
                'db_table': 'music',
                'verbose_name': '外链音乐',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='1~20个字', max_length=20, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='详情')),
                ('add', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='最近修改')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可见')),
            ],
            options={
                'verbose_name_plural': '公告',
                'db_table': 'notice',
                'verbose_name': '公告',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(help_text='1~12个字', max_length=12, unique=True, verbose_name='标签')),
                ('add', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('mod', models.DateTimeField(auto_now=True, verbose_name='最近修改')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
            options={
                'verbose_name_plural': '标签',
                'db_table': 'tag',
                'verbose_name': '标签',
            },
        ),
        migrations.AlterUniqueTogether(
            name='music',
            unique_together={('name', 'author')},
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_active': True}, related_name='tbooks', to='db.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='blog',
            name='cat',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cblogs', to='db.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='blog',
            name='music',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mblogs', to='db.Music', verbose_name='背景音乐'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_active': True}, related_name='tblogs', to='db.Tag', verbose_name='标签'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
            ],
            options={
                'verbose_name_plural': '我的账号',
                'indexes': [],
                'verbose_name': '我的账号',
                'proxy': True,
            },
            bases=('db.useraccount',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorBlog',
            fields=[
            ],
            options={
                'verbose_name_plural': '我的博客',
                'indexes': [],
                'verbose_name': '我的博客',
                'proxy': True,
            },
            bases=('db.blog',),
        ),
        migrations.CreateModel(
            name='AuthorBook',
            fields=[
            ],
            options={
                'verbose_name_plural': '我的专题',
                'indexes': [],
                'verbose_name': '我的专题',
                'proxy': True,
            },
            bases=('db.book',),
        ),
        migrations.CreateModel(
            name='AuthorChapter',
            fields=[
            ],
            options={
                'verbose_name_plural': '专题章节',
                'indexes': [],
                'verbose_name': '专题章节',
                'proxy': True,
            },
            bases=('db.chapter',),
        ),
        migrations.CreateModel(
            name='TipAd',
            fields=[
            ],
            options={
                'verbose_name_plural': '长条广告',
                'indexes': [],
                'verbose_name': '长条广告',
                'proxy': True,
            },
            bases=('db.advertisement',),
        ),
    ]
