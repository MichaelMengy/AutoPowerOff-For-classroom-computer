# Readme.md of AutoPowerOff-For-classroom-computer

<center>用于win电脑的自动关机小脚本<center/>

## 各个文件说明

| AutoPowerOff.py | 主程序位置，在这里设置自动关机规则     |
| :-------------: | -------------------------------------- |
|   get_time.py   | 获取小时分钟秒的封装                   |
|  schedules.py   | 计划任务封装以及判断任务是否过期的实现 |

---

## 安装

没啥好说的，装了python就行

---

## 设置

直接更改*AutoPowerOff.py* 里面的**OFFTIMES**列表内容即可

默认规则按照*高中部2020-2021学年度上学期高二年级*  的作息时间编写

### 规则格式

一个item为一条规则，格式如下：

```python
time_rule(enabled,hh,mm,ss,operation,specific_rule,spe_list,cmd)
```

|    参数名     | 类型 | 含义/范围                                                    |
| :-----------: | :--: | ------------------------------------------------------------ |
|    enabled    | bool | 该规则是否启用                                               |
|      hh       | int  | hh,mm,ss依次为关机规则触发的时刻 时--分--秒                  |
|      mm       | int  | 见上↑                                                        |
|      ss       | int  | 见上↑                                                        |
|   operation   | int  | 规则触发时执行的操作：0 = 什么都不做 1 = 没有任何警告直接关机 2 = 弹窗警告 一分钟后关机 |
| specific_rule | int  | 附加规则，目前支持的有：0 = 无附加规则，1 = 规则将在每周星期x触发（$x \in spelist)$，2 = 规则将在每周星期y触发$(y \notin spelist)$ |
|   spe_list    | list | 当specific_rule = 0 时，随便填；否则按照上面的要求填写       |
|      cmd      | str  | 自定义的cmd命令                                              |

你也可以使用已经定义好的shutdown_now，shutdown_warn，run_custom_cmd，no_specific，run_only_on，run_except 来替换规则里的参数，使规则对人更友好

##  注意：必须按照时间顺序排序规则！

请不要在规则里填写亿些奇奇怪怪的数据……否则程序会报错……

就先写到这里吧……