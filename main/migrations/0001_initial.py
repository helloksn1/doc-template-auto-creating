# Generated by Django 4.0.3 on 2022-03-16 08:36

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
            name='PHChaptor0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d0', models.CharField(blank=True, max_length=30, null=True)),
                ('d1', models.CharField(blank=True, max_length=30, null=True)),
                ('d1_m', models.CharField(blank=True, max_length=30, null=True)),
                ('d2', models.CharField(blank=True, max_length=30, null=True, verbose_name='调查评估部门')),
                ('d3_m', models.CharField(blank=True, max_length=30, null=True, verbose_name='主调查人')),
                ('d3_s', models.CharField(blank=True, max_length=30, null=True, verbose_name='调查评估人员')),
                ('d4_0', models.CharField(blank=True, max_length=30, null=True)),
                ('d4_1', models.CharField(blank=True, max_length=30, null=True)),
                ('d5', models.CharField(blank=True, max_length=30, null=True, verbose_name='分管行长')),
                ('d6_y', models.CharField(blank=True, max_length=30, null=True)),
                ('d6_m', models.CharField(blank=True, max_length=30, null=True)),
                ('dr0_m', models.CharField(blank=True, max_length=30, null=True)),
                ('dr0_s', models.CharField(blank=True, max_length=30, null=True)),
                ('l0', models.CharField(blank=True, max_length=30, null=True)),
                ('l1', models.CharField(blank=True, max_length=30, null=True)),
                ('l2', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PHChaptor1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m110', models.CharField(blank=True, max_length=30, null=True, verbose_name='项目名称')),
                ('m120', models.CharField(blank=True, max_length=30, null=True)),
                ('m121', models.CharField(blank=True, max_length=30, null=True)),
                ('m122', models.CharField(blank=True, max_length=30, null=True)),
                ('m123', models.CharField(blank=True, max_length=30, null=True)),
                ('m124', models.CharField(blank=True, max_length=30, null=True)),
                ('m125', models.CharField(blank=True, max_length=30, null=True)),
                ('m126', models.CharField(blank=True, max_length=30, null=True)),
                ('m127', models.CharField(blank=True, max_length=30, null=True)),
                ('m128', models.CharField(blank=True, max_length=30, null=True)),
                ('m129', models.CharField(blank=True, max_length=30, null=True)),
                ('m1210', models.CharField(blank=True, max_length=30, null=True)),
                ('m1211', models.CharField(blank=True, max_length=30, null=True)),
                ('m1212', models.CharField(blank=True, max_length=30, null=True)),
                ('m1213', models.CharField(blank=True, max_length=30, null=True)),
                ('m130', models.CharField(blank=True, max_length=30, null=True)),
                ('m131', models.CharField(blank=True, max_length=30, null=True)),
                ('m140', models.CharField(blank=True, max_length=30, null=True)),
                ('m141', models.CharField(blank=True, max_length=30, null=True)),
                ('m150', models.CharField(blank=True, max_length=30, null=True)),
                ('m151', models.CharField(blank=True, max_length=30, null=True)),
                ('m152', models.CharField(blank=True, max_length=30, null=True)),
                ('m153', models.CharField(blank=True, max_length=30, null=True)),
                ('m154', models.CharField(blank=True, max_length=30, null=True)),
                ('i155', models.ImageField(blank=True, max_length=300, null=True, upload_to='')),
                ('i156', models.ImageField(blank=True, max_length=300, null=True, upload_to='')),
                ('m160', models.CharField(blank=True, max_length=30, null=True)),
                ('m161', models.CharField(blank=True, max_length=30, null=True)),
                ('m162', models.CharField(blank=True, max_length=30, null=True)),
                ('m170', models.CharField(blank=True, max_length=30, null=True)),
                ('m171', models.CharField(blank=True, max_length=30, null=True)),
                ('m172', models.CharField(blank=True, max_length=30, null=True)),
                ('m180', models.CharField(blank=True, max_length=30, null=True)),
                ('m181', models.CharField(blank=True, max_length=30, null=True)),
                ('m182', models.CharField(blank=True, max_length=30, null=True)),
                ('m183', models.CharField(blank=True, max_length=30, null=True)),
                ('m184', models.CharField(blank=True, max_length=30, null=True)),
                ('m185', models.CharField(blank=True, max_length=30, null=True)),
                ('m186', models.CharField(blank=True, max_length=30, null=True)),
                ('m187', models.CharField(blank=True, max_length=30, null=True)),
                ('m188', models.CharField(blank=True, max_length=30, null=True)),
                ('m189', models.CharField(blank=True, max_length=30, null=True)),
                ('m1810', models.CharField(blank=True, max_length=30, null=True)),
                ('m1811', models.CharField(blank=True, max_length=30, null=True)),
                ('m1812', models.CharField(blank=True, max_length=30, null=True)),
                ('m1813', models.CharField(blank=True, max_length=30, null=True)),
                ('m1814', models.CharField(blank=True, max_length=30, null=True)),
                ('m1815', models.CharField(blank=True, max_length=30, null=True)),
                ('m1816', models.CharField(blank=True, max_length=30, null=True)),
                ('m1817', models.CharField(blank=True, max_length=30, null=True)),
                ('m190', models.CharField(blank=True, max_length=30, null=True)),
                ('m191', models.CharField(blank=True, max_length=30, null=True)),
                ('m192', models.CharField(blank=True, max_length=30, null=True)),
                ('m193', models.CharField(blank=True, max_length=30, null=True)),
                ('m194', models.CharField(blank=True, max_length=30, null=True)),
                ('m195', models.CharField(blank=True, max_length=30, null=True)),
                ('m196', models.CharField(blank=True, max_length=30, null=True)),
                ('m197', models.CharField(blank=True, max_length=30, null=True)),
                ('m198', models.CharField(blank=True, max_length=30, null=True)),
                ('m199', models.CharField(blank=True, max_length=30, null=True)),
                ('m1910', models.CharField(blank=True, max_length=30, null=True)),
                ('m1911', models.CharField(blank=True, max_length=30, null=True)),
                ('m1912', models.CharField(blank=True, max_length=30, null=True)),
                ('m1913', models.CharField(blank=True, max_length=30, null=True)),
                ('m1914', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PHChaptor2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m2_1_0', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_1', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_2', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_3', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_4', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_5', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_6', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_7', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_8', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_9', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_1_10', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_0', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_1', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_2', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_3', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_4', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_5', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_6', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_7', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_8', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_9', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_10', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_11', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_2_12', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_3_0', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_3_1', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_3_2', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_3_3', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_3_4', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_1_0', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_1_1', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_1_2', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_1_3', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_1_4', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_1_5', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_0', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_1', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_2', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_3', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_4', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_5', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_6', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_7', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_8', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_9', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_10', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_11', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_12', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_13', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_14', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_15', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_16', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_17', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_18', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_19', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_20', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_21', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_22', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_23', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_24', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_25', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_26', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_27', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_28', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_29', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_30', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_31', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_32', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_33', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_34', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_35', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_36', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_37', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_38', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_39', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_40', models.CharField(blank=True, max_length=30, null=True)),
                ('m2_4_2_41', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(blank=True, max_length=200, null=True)),
                ('sex', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=30)),
                ('chaptor0', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.phchaptor0')),
                ('chaptor1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.phchaptor1')),
                ('chaptor2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.phchaptor2')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '调查评估报告',
                'db_table': 'main_PlaceHolder',
            },
        ),
    ]
