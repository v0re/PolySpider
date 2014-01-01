#!/usr/bin/env python
#coding:gbk

'''
使用方法：
    由于不同的应用商店对应的分类不同，抓取到的应用进行分类整理也不能完全按照分类名来新建分类
    为了统一分类，采取91助手的分类作为默认分类方式，并为每一个分类定义一个ID
    建立一个字典，key为应用市场中抓取的分类名，value为对应的分类ID
    当所有市场中的分类名称都已经在字典中定义以后，就可以直接通过抓取分类名来将应用对应到我们的分类列表中来。
'''
'''
应用名称    ID(后两位为00，预留，如果有子分类的话，可以利用，比如游戏有自分类的话可以是4601，4602这样)

其它工具    1000
系统工具    1100
日常应用    1200
影音媒体    1300
视频软件    1400
图书教育    1500
网络应用    1600
即时聊天    1700
音频软件    1800
书籍杂志    1900
社区交友    2000
生活健康    2100
图像处理    2200
查询参考    2300
系统管理    2400
浏览辅助    2500
主题美化    2600
地图导航    2700
安全防范    2800
新闻阅读    2900
照相增强    3000
儿童教学    3100
电子词典    3200
时钟日历    3300
理财工具    3400
中文输入    3500
通话辅助    3600
名片管理    3700
文档处理    3800
文件管理    3900
日程备忘    4000
短信增强    4100
词典查询    4200
计算工具    4300
蓝牙红外    4400
网络通信    4500
游戏        4600

'''

##比如将其分类设置为需要额外一些工作来进行确认的分类
#比如一个应用如果是办公分类，首先查看其是否已经gab到数据库中，如果数据库中对这个应用已经有记录，那么直接那个记录我在想，如果有些分类比较笼统话，是否可以做出一定的策略，而不是将该分类之间确定为某一个我们的分类
#比如App_star中的办公分类，实际上是一个笼统概念，无法直接与我们的分类进行对应
#比如将其分类设置为需要额外一些工作来进行确认的分类
#比如一个应用如果是办公分类，首先查看其是否已经gab到数据库中，如果数据库中对这个应用已经有记录，那么直接那个记录来分类
#如果没有记录，则指定某个默认分类来记录，等待别的应用商店上传该应用，来分类，或者该应用进行人工分类的操作等等
CATEGORY = {
    ## Common
    '其他'      :   '[1000]',
    ## App_star分类字典 By Eric Wang
    '阅读资讯'  :   '[1900]',
    '电子书'    :   '[1500,1900]',
    '输入法'    :   '[3500]',
    '休闲益智'  :   '[4600]',
    '动作竞技'  :   '[4600]',
    '体育竞速'  :   '[4600]',
    '健康美食'  :   '[2100]',
    '系统工具'  :   '[1100]',
    '主题桌面'  :   '[2600]',
    '音乐视频'  :   '[1300]',
    '社交'      :   '[2000]',
    '办公'      :   '[1200]',
    '交通地图'  :   '[2700]',
    ## 应用宝
    ## 小米商城
    '影音视听':'[1300,1400]',
    '图书与阅读':'[1500]',
    '效率办公':'[3800]',
    '生活':'[2100]',
    '摄影摄像':'[3000]',
    '体育运动':'[2100]',
    '娱乐消遣':'[1300]',
    '实用工具':'[1100]',
    '聊天与社交':'[2000]',
    '学习与教育':'[3100]',
    '时尚与购物':'[1200]',
    '旅行与交通':'[2700]',
    '医疗与健康':'[2100]',
    '新闻':'[2900]',
    '理财':'[3400]',
    '策略':'[4600]',
    '竞速':'[4600]',
    '棋牌':'[4600]',
    '音乐游戏':'[4600]',
    '飞行模式':'[4600]',
    '动作冒险':'[4600]',
    '角色扮演':'[4600]',
    '体育运动':'[4600]',
    '益智解密':'[4600]',
    '重力感应':'[4600]',
    #安卓市场
    '工具':'[1100]',
}

def getCategoryIds(category_name):
    if not CATEGORY.get(category_name):
        #如果没有，则un_record_category.yml记录该分类
        print "分类：%s" %category_name
        flag = True
        category_map = {}
        for line in open('un_record_category.txt','r'): 
            if line.strip() == category_name:
                flag = False
                break
            category_map[line.strip()] = 1
	category_map[category_name] = 1
        if flag:
            with open('un_record_category.txt','w') as f: 
                for key in category_map.keys(): 
                    f.write(key + "\n")
        return ""
        
    return CATEGORY.get(category_name)
