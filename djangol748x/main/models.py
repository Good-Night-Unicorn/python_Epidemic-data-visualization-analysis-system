#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    yonghudianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户电话' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    '''
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    yonghuxingming=VARCHAR
    xingbie=VARCHAR
    yonghudianhua=VARCHAR
    touxiang=VARCHAR
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class yuangong(BaseModel):
    __doc__ = u'''yuangong'''
    __tablename__ = 'yuangong'

    __loginUser__='yuangongzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yuangongzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yuangongzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='员工账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yuangongxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='员工姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    yuangongdianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='员工电话' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    '''
    yuangongzhanghao=VARCHAR
    mima=VARCHAR
    yuangongxingming=VARCHAR
    xingbie=VARCHAR
    yuangongdianhua=VARCHAR
    touxiang=VARCHAR
    '''
    class Meta:
        db_table = 'yuangong'
        verbose_name = verbose_name_plural = '员工'
class yiqingxinxi(BaseModel):
    __doc__ = u'''yiqingxinxi'''
    __tablename__ = 'yiqingxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    diqu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地区' )
    tupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    fabushijian=models.DateField   (  null=True, unique=False, verbose_name='发布时间' )
    xinzengrenshu=models.IntegerField  (  null=True, unique=False, verbose_name='新增人数' )
    quezhenrenshu=models.IntegerField  (  null=True, unique=False, verbose_name='确诊人数' )
    xinzengwuzhengzhuang=models.IntegerField  (  null=True, unique=False, verbose_name='新增无症状' )
    fengxianchengdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='风险程度' )
    xiangguanlianjie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='相关链接' )
    yiqingxiangqing=models.TextField   (  null=True, unique=False, verbose_name='疫情详情' )
    '''
    diqu=VARCHAR
    tupian=VARCHAR
    fabushijian=Date
    xinzengrenshu=Integer
    quezhenrenshu=Integer
    xinzengwuzhengzhuang=Integer
    fengxianchengdu=VARCHAR
    xiangguanlianjie=VARCHAR
    yiqingxiangqing=Text
    '''
    class Meta:
        db_table = 'yiqingxinxi'
        verbose_name = verbose_name_plural = '疫情信息'
class hesuanjiance(BaseModel):
    __doc__ = u'''hesuanjiance'''
    __tablename__ = 'hesuanjiance'



    __authTables__={'yuangongzhanghao':'yuangong',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    bianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='编号' )
    biaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='标题' )
    fengmian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='封面' )
    fabushijian=models.DateField   (  null=True, unique=False, verbose_name='发布时间' )
    jiancedizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='检测地址' )
    xiangqing=models.TextField   (  null=True, unique=False, verbose_name='详情' )
    yuangongzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='员工账号' )
    yuangongxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='员工姓名' )
    '''
    bianhao=VARCHAR
    biaoti=VARCHAR
    fengmian=VARCHAR
    fabushijian=Date
    jiancedizhi=VARCHAR
    xiangqing=Text
    yuangongzhanghao=VARCHAR
    yuangongxingming=VARCHAR
    '''
    class Meta:
        db_table = 'hesuanjiance'
        verbose_name = verbose_name_plural = '核酸检测'
class jianceyuyue(BaseModel):
    __doc__ = u'''jianceyuyue'''
    __tablename__ = 'jianceyuyue'



    __authTables__={'yonghuzhanghao':'yonghu','yuangongzhanghao':'yuangong',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yuyuebianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='预约编号' )
    biaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='标题' )
    yuyueshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='预约时间' )
    yuyuebeizhu=models.TextField   (  null=True, unique=False, verbose_name='预约备注' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    yuangongzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='员工账号' )
    yuangongxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='员工姓名' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    yuyuebianhao=VARCHAR
    biaoti=VARCHAR
    yuyueshijian=DateTime
    yuyuebeizhu=Text
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    yuangongzhanghao=VARCHAR
    yuangongxingming=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'jianceyuyue'
        verbose_name = verbose_name_plural = '检测预约'
class jiancejieguo(BaseModel):
    __doc__ = u'''jiancejieguo'''
    __tablename__ = 'jiancejieguo'



    __authTables__={'yuangongzhanghao':'yuangong','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiancebianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='检测编号' )
    biaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='标题' )
    jianceshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='检测时间' )
    jiancejieguo=models.CharField ( max_length=255, null=True, unique=False, verbose_name='检测结果' )
    yuangongzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='员工账号' )
    yuangongxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='员工姓名' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    '''
    jiancebianhao=VARCHAR
    biaoti=VARCHAR
    jianceshijian=DateTime
    jiancejieguo=VARCHAR
    yuangongzhanghao=VARCHAR
    yuangongxingming=VARCHAR
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    '''
    class Meta:
        db_table = 'jiancejieguo'
        verbose_name = verbose_name_plural = '检测结果'
class xingchengxinxi(BaseModel):
    __doc__ = u'''xingchengxinxi'''
    __tablename__ = 'xingchengxinxi'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    chufashijian=models.DateTimeField  (  null=True, unique=False, verbose_name='出发时间' )
    chufadi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='出发地' )
    mudedi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='目的地' )
    fanhuishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='返回时间' )
    fengxiandiqu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='风险地区' )
    jiaotonggongju=models.CharField ( max_length=255, null=True, unique=False, verbose_name='交通工具' )
    dengjiriqi=models.DateField   (  null=True, unique=False, verbose_name='登记日期' )
    xingchengjilu=models.TextField   (  null=True, unique=False, verbose_name='行程记录' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    xingbie=VARCHAR
    chufashijian=DateTime
    chufadi=VARCHAR
    mudedi=VARCHAR
    fanhuishijian=DateTime
    fengxiandiqu=VARCHAR
    jiaotonggongju=VARCHAR
    dengjiriqi=Date
    xingchengjilu=Text
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'xingchengxinxi'
        verbose_name = verbose_name_plural = '行程信息'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '新闻资讯'
