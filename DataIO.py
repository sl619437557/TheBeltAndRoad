#encoding=utf-8
import pymysql
url='https://www.yidaiyilu.gov.cn/xwzx/gnxw/149482.htm'
title='担当历史责任，共创历史伟业：评习近平主席在第七十五届联合国大会一般性辩论上的重要讲话'
date='2020-09-23 09:14:11'
source='中国新闻网'
content='历史接力棒已经传到我们这一代人手中，我们必须作出无愧于人民、无愧于历史的抉择。”22日，习近平主席在第七十五届联合国大会一般性辩论上发表重要讲话，提出抗击新冠肺炎疫情的4点倡议，深刻总结疫情带来的4' \
        '点重要启示，进一步回答了“世界怎么了、我们怎么办”的时代之问，郑重宣布中国支持联合国发挥核心作用的4项重大举措。讲话秉持人类命运共同体理念，把握时代大势、彰显中国智慧、展现中国担当，引发国际社会广泛共鸣。	' \
        '当前，人类正在同新冠肺炎疫情进行斗争，这对全世界是一次严峻考验。病毒是人类共同的敌人，唯有以人为本、团结合作，才能战而胜之。正如习近平主席指出的，面对疫情，要践行人民至上、生命至上理念，要加强团结、同舟共济，要制定全面和常态化防控措施，要关心和照顾发展中国家特别是非洲国家。这4点倡议，坚持以人民中心，统筹疫情防控和经济社会发展，倡导科学精神和合作精神，既凝结着中国抗击疫情的成功经验，又针对全球抗疫面临的突出问题提出破解之策，有利于推动国际抗疫合作，为维护全球公共卫生安全注入强大正能量。	一部人类社会发展史，就是一部不断战胜各种挑战和困难的历史。尽管新冠肺炎疫情全球大流行和世界百年未有之大变局相互影响，但和平与发展的时代主题没有变，各国人民和平发展合作共赢的期待更加强烈。面对不断上升的全球性挑战，我们必须携手应对、共克时艰，共创历史伟业，共建美好家园。	“欲粟者务时，欲治者因势。”把握世界发展的“时”与“势”，厘清人类面对什么样的世界，才能沿着正确方向行稳致远。这场疫情启示我们，我们生活在一个互联互通、休戚与共的地球村里，经济全球化是客观现实和历史潮流。各国紧密相连，人类命运与共，必须跳出小圈子和零和博弈思维，树立你中有我、我中有你的命运共同体意识，树立大家庭和合作共赢理念。经济全球化是不可阻挡的历史大势，世界退不回彼此封闭孤立的状态，更不可能被人为割裂。顺应历史潮流，必须维护公平正义，直面贫富差距、发展鸿沟等重大问题，使发展既平衡又充分，让发展成果更公平惠及各国人民；必须秉持开放包容理念，旗帜鲜明反对单边主义、保护主义，坚定不移构建开放型世界经济。让和平的薪火代代相传，让发展的动力源源不断，让文明的光芒熠熠生辉，这是各国人民的热切期盼，也是各国政治家应有的责任担当。	“世异则事异，事异则备变。”当今世界正经历百年未有之大变局，唯有准确识变、科学应变、主动求变，方能于变局中开新局。疫情如同一面放大镜，照出人类发展方式和生活方式的痼疾，照出全球治理体系的短板，告诫我们要勇于变革、善于行动。只讲索取不讲投入、只讲发展不讲保护、只讲利用不讲修复的老路不可持续，人类需要一场自我革命，加快形成绿色发展方式和生活方式，推动疫情后世界经济“绿色复苏”，汇聚起可持续发展的强大合力。全球治理体系亟待改革和完善，必须坚持走多边主义道路，维护以联合国为核心的国际体系，秉持共商共建共享原则，推动全球治理朝着更加公平有效的方向发展，使全球治理体系符合变化了的世界政治经济，满足应对全球性挑战的现实需要，顺应和平发展合作共赢的历史趋势。	作为世界上最大的发展中国家，中国走的是和平发展、开放发展、合作发展、共同发展的正道，行的是“为人类谋大同”的大道。习近平主席2015年在联合国成立70周年系列峰会上，宣布了支持联合国事业的一系列重大倡议和举措，目前均已得到落实。在第七十五届联合国大会上，习近平主席再次提出支持联合国在国际事务中发挥核心作用的4项重大举措。无论是向联合国新冠肺炎疫情全球人道主义应对计划提供资金支持，还是推动南南合作，或者是助力落实《联合国2030年可持续发展议程》，在承担大国责任、增进人类福祉方面，中国始终是知行合一的行动派、实干家，坚定不移做世界和平的建设者、全球发展的贡献者、国际秩序的维护者。	团结就是力量，正义不可战胜。站在历史的十字路口，各国人民携手前行，推动构建新型国际关系，推动构建人类命运共同体，必将把人类和平与发展的崇高事业不断推向前进，共同创造世界更加美好的未来。	（原标题：担当历史责任，共创历史伟业：评习近平主席在第七十五届联合国大会一般性辩论上的重要讲话 '


def insert(values):
    try:
        db = pymysql.connect("localhost", "root", "1205", "news")
        cursor = db.cursor()
        sql='insert into localnews(url,title,date,source,content) values(%s,%s,%s,%s,%s)'
        values=values
        cursor.execute(sql,values)
        db.commit()
        cursor.close()
        db.close()
        print('爬取成功'+values[0])
    except Exception as e:
        print(e)