from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org = models.CharField(null=True, blank=True, max_length=200)
    sex = models.BooleanField(default=True)


class PHChaptor0(models.Model):
    # 封页
    d0 = models.CharField(max_length=30, null=True, blank=True) # 公司名
    d1 = models.CharField(max_length=30, null=True, blank=True) # 万元
    d1_m = models.CharField(max_length=30, null=True, blank=True)
    d2 = models.CharField('调查评估部门', max_length=30, null=True, blank=True) # 调查评估部门
    d3_m = models.CharField('主调查人', max_length=30, null=True, blank=True) # 调查评估人员 主调查人
    d3_s = models.CharField('调查评估人员', max_length=30, null=True, blank=True) # 调查评估人员
    d4_0 = models.CharField(max_length=30, null=True, blank=True) # 调查评估部门负责人0
    d4_1 = models.CharField(max_length=30, null=True, blank=True) # 调查评估部门负责人1
    d5 = models.CharField('分管行长', max_length=30, null=True, blank=True) # 调查评估部门分管行长
    d6_y = models.CharField(max_length=30, null=True, blank=True) # 调查评估时间 年
    d6_m = models.CharField(max_length=30, null=True, blank=True) # 调查评估时间 月
    # 评估人员
    dr0_m = models.CharField(max_length=30, null=True, blank=True) # 调查评估中心 主调查人
    dr0_s = models.CharField(max_length=30, null=True, blank=True) # 调查评估中心 人
    # 目录
    l0 = models.CharField(max_length=30, null=True, blank=True)
    l1 = models.CharField(max_length=30, null=True, blank=True)
    l2 = models.CharField(max_length=30, null=True, blank=True)


class PHChaptor1(models.Model):
    # 第一章
    # 1.1 项目名称
    m110 = models.CharField('项目名称', max_length=30, null=True, blank=True) # 项目名称
    # 1.2 项目立项及可研批复情况
    m120 = models.CharField(max_length=30, null=True, blank=True)
    m121 = models.CharField(max_length=30, null=True, blank=True)
    m122 = models.CharField(max_length=30, null=True, blank=True)
    m123 = models.CharField(max_length=30, null=True, blank=True)
    m124 = models.CharField(max_length=30, null=True, blank=True)
    m125 = models.CharField(max_length=30, null=True, blank=True)
    m126 = models.CharField(max_length=30, null=True, blank=True)
    m127 = models.CharField(max_length=30, null=True, blank=True)
    m128 = models.CharField(max_length=30, null=True, blank=True)
    m129 = models.CharField(max_length=30, null=True, blank=True)
    m1210 = models.CharField(max_length=30, null=True, blank=True)
    m1211 = models.CharField(max_length=30, null=True, blank=True)
    m1212 = models.CharField(max_length=30, null=True, blank=True)
    m1213 = models.CharField(max_length=30, null=True, blank=True)
    # 1.3 项目性质及类型
    m130 = models.CharField(max_length=30, null=True, blank=True) # **法人
    m131 = models.CharField(max_length=30, null=True, blank=True) # **项目
    # 1.4 项目承贷主体
    m140 = models.CharField(max_length=30, null=True, blank=True) # **公司
    m141 = models.CharField(max_length=30, null=True, blank=True) # 以下简称“**公司”
    # 1.5 项目建设地址
    m150 = models.CharField(max_length=30, null=True, blank=True) # 位于****
    m151 = models.CharField(max_length=30, null=True, blank=True) # 代码为**
    m152 = models.CharField(max_length=30, null=True, blank=True) # 位于****
    m153 = models.CharField(max_length=30, null=True, blank=True) # 分类代码为**
    m154 = models.CharField(max_length=30, null=True, blank=True) # **区（县）
    i155 = models.ImageField(max_length=300, null=True, blank=True)
    i156 = models.ImageField(max_length=300, null=True, blank=True)
    # 1.6 项目建设内容及规模
    m160 = models.CharField(max_length=30, null=True, blank=True) # 根据《**批复》
    m161 = models.CharField(max_length=30, null=True, blank=True) # 包括******工程
    m162 = models.CharField(max_length=30, null=True, blank=True) # 建设规模****
    # 1.7 项目运作模式
    m170 = models.CharField(max_length=30, null=True, blank=True) # 本项目实行“****”模式
    m171 = models.CharField(max_length=30, null=True, blank=True) # 由****公司
    m172 = models.CharField(max_length=30, null=True, blank=True) # 由****收益进行偿还
    # 1.8 项目投资规模及资金筹措
    m180 = models.CharField(max_length=30, null=True, blank=True)
    m181 = models.CharField(max_length=30, null=True, blank=True)
    m182 = models.CharField(max_length=30, null=True, blank=True)
    m183 = models.CharField(max_length=30, null=True, blank=True)
    m184 = models.CharField(max_length=30, null=True, blank=True)
    m185 = models.CharField(max_length=30, null=True, blank=True)
    m186 = models.CharField(max_length=30, null=True, blank=True)
    m187 = models.CharField(max_length=30, null=True, blank=True)
    m188 = models.CharField(max_length=30, null=True, blank=True)
    m189 = models.CharField(max_length=30, null=True, blank=True)
    m1810 = models.CharField(max_length=30, null=True, blank=True)
    m1811 = models.CharField(max_length=30, null=True, blank=True)
    m1812 = models.CharField(max_length=30, null=True, blank=True)
    m1813 = models.CharField(max_length=30, null=True, blank=True)
    m1814 = models.CharField(max_length=30, null=True, blank=True)
    m1815 = models.CharField(max_length=30, null=True, blank=True)
    m1816 = models.CharField(max_length=30, null=True, blank=True)
    m1817 = models.CharField(max_length=30, null=True, blank=True)
    # 1.9 申请贷款情况及贷款建议
    m190 = models.CharField(max_length=30, null=True, blank=True)
    m191 = models.CharField(max_length=30, null=True, blank=True)
    m192 = models.CharField(max_length=30, null=True, blank=True)
    m193 = models.CharField(max_length=30, null=True, blank=True)
    m194 = models.CharField(max_length=30, null=True, blank=True)
    m195 = models.CharField(max_length=30, null=True, blank=True)
    m196 = models.CharField(max_length=30, null=True, blank=True)
    m197 = models.CharField(max_length=30, null=True, blank=True)
    m198 = models.CharField(max_length=30, null=True, blank=True)
    m199 = models.CharField(max_length=30, null=True, blank=True)
    m1910 = models.CharField(max_length=30, null=True, blank=True)
    m1911 = models.CharField(max_length=30, null=True, blank=True)
    m1912 = models.CharField(max_length=30, null=True, blank=True)
    m1913 = models.CharField(max_length=30, null=True, blank=True)
    m1914 = models.CharField(max_length=30, null=True, blank=True)


class PHChaptor2(models.Model):
    # 第二章
    # 2.1 客户概况
    m2_1_0 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_1 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_2 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_3 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_4 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_5 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_6 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_7 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_8 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_9 = models.CharField(max_length=30, null=True, blank=True)
    m2_1_10 = models.CharField(max_length=30, null=True, blank=True)
    # 2.2 集团客户认定情况
    m2_2_0 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_1 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_2 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_3 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_4 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_5 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_6 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_7 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_8 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_9 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_10 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_11 = models.CharField(max_length=30, null=True, blank=True)
    m2_2_12 = models.CharField(max_length=30, null=True, blank=True)
    # 2.3 股权结构
    m2_3_0 = models.CharField(max_length=30, null=True, blank=True)
    m2_3_1 = models.CharField(max_length=30, null=True, blank=True)
    m2_3_2 = models.CharField(max_length=30, null=True, blank=True)
    m2_3_3 = models.CharField(max_length=30, null=True, blank=True)
    m2_3_4 = models.CharField(max_length=30, null=True, blank=True)
    # 2.4 组织结构及经营人员素质
    # 2.4.1 组织结构
    m2_4_1_0 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_1_1 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_1_2 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_1_3 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_1_4 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_1_5 = models.CharField(max_length=30, null=True, blank=True)
    # 2.4.2 经营人员素质
    m2_4_2_0 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_1 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_2 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_3 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_4 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_5 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_6 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_7 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_8 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_9 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_10 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_11 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_12 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_13 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_14 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_15 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_16 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_17 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_18 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_19 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_20 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_21 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_22 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_23 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_24 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_25 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_26 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_27 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_28 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_29 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_30 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_31 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_32 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_33 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_34 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_35 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_36 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_37 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_38 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_39 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_40 = models.CharField(max_length=30, null=True, blank=True)
    m2_4_2_41 = models.CharField(max_length=30, null=True, blank=True)


class PlaceHolder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    filename = models.CharField(max_length=30)
    chaptor0 = models.OneToOneField(PHChaptor0, on_delete=models.CASCADE)
    chaptor1 = models.OneToOneField(PHChaptor1, on_delete=models.CASCADE)
    chaptor2 = models.OneToOneField(PHChaptor2, on_delete=models.CASCADE)

    class Meta:
        db_table = 'main_PlaceHolder'
        verbose_name_plural = '调查评估报告'

    def get_absolute_url(self):
        print('url here')
        # return reverse('detail', kwargs={ 'pk': self.pk })
        return reverse('list')
