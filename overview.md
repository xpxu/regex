###概述
正则表达式在计算机科学中，是指一个用来描述或者匹配一系列符合某个句法规则的字符串的 单个字符串。在很多文本编辑器或其他工具里，正则表达式通常被用来检索和/或替换那些符合某个模式的文本内容。许多程序设计语言都支持利用正则表达式进行 字符串操作。例如，在Perl中就内建了一个功能强大的正则表达式引擎。正则表达式这个概念最初是由Unix中的工具软件（例如sed和grep）普及开 的。正则表达式通常缩写成“regex”，单数有regexp、regex，复数有regexps、regexes、regexen。这些是正则表达式的 定义。 由于起源于unix系统，因此很多语法规则一样的。但是随着逐渐发展，后来扩展出以下几个类型。了解这些对于学习正则表达式。
### 一、正则表达式分类
1、基本的正则表达式（Basic Regular Expression 又叫 Basic RegEx  简称 BREs）
2、扩展的正则表达式（Extended Regular Expression 又叫 Extended RegEx 简称 EREs）
3、Perl 的正则表达式（Perl Regular Expression 又叫 Perl RegEx 简称 PREs）
###二、Linux 中常用文本工具与正则表达式的关系
grep 支持：BREs、EREs、PREs 正则表达式
grep 指令后不跟任何参数，则表示要使用 ”BREs“
grep 指令后跟 ”-E" 参数，则表示要使用 “EREs“
grep 指令后跟 “-P" 参数，则表示要使用 “PREs"
###三、3种类型正则表达式比较
注意Python的re模块提供的就是PRE.
[BRE/ERE/PRE比较](http://www.cnblogs.com/chengmo/archive/2010/10/10/1847287.html)
