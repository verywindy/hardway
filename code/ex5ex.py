# -*- coding:utf-8 -*-
name = 'Zed A.Shaw'
age = 35 # not a lie 
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

my_height_centimeter = height * 2.54 # centimeter(厘米） 1英寸=2.54厘米，用Python的数字计算功能实现了英寸到厘米的转换，下一句实现了磅到千克的转换
my_weight_kilo = weight * 0.4536 # kilo(千克）, 1磅=0.4536千克
print "let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeter tall." % my_height_centimeter # 输出厘米
print "He's %r pounds heavy." % weight #输出千克
print "He's %.1f kilo heavy." % my_weight_kilo
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky,try to get it exactly right
print "If i add %s,%f,and %x I get %d ." % (age,height,weight,age + height + weight)
