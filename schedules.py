import time


class time_rule:

    """
    Class used for determining a shutdown rule

    ____________

    Args:

        enabled: bool 任务是否执行

        hh: int 触发时刻-时

        mm: int 触发时刻-分

        ss: int 触发时刻-秒

        operation: int 任务操作: 0 = 直接关机|1 = 不执行任何操作|2 = 延迟一分钟关机|3 = 运行自定义cmd

        specific rule: int 附加条件: 0 = 没有任何附加条件|1 = 只有在以下星期x触发 | 2 = 不在以下星期x触发

        spe list: list 储存附加条件的列表
        cmd: str 自定义命令行 
    """

    def __init__(self,enabled: bool,hh: int,mm: int,ss: int,operation: int,specific_rule: int,spe_list: list,cmd :str) -> None:
        self.enabled = enabled
        self.hh = hh
        self.mm = mm
        self.ss = ss
        self.operation = operation
        self.specific = specific_rule
        self.spe_list = spe_list
        self.cmd = cmd
        pass
def check(hour:int,minute:int,second:int,dayOfWeek:int,set: time_rule) -> bool:
    '''
    Checks whether the rule will be executed and throw errors
    '''
    errors = False
    if (set.hh > 24 or set.hh <0) or (set.mm >59 or set.mm < 0) or (set.ss > 59 or set.ss < 0):
        errors = True
        raise ValueError("Invalid time!")
        pass
    if (set.operation > 2 or set.operation < 0) or (set.specific > 2 or set.specific < 0):
        errors = True
        raise ValueError("Invalid operation or specific rule!")
    if (set.specific != 0 and len(set.spe_list) == 0):
        raise BaseException("specific rule not found")
    if(set.operation != 0):
        for i in set.spe_list:
            if i > 7 or i < 1:
                raise ValueError("Invalid DayOfWeek in specific rule !")


    if set.enabled == False:
        return False
    if hour > set.hh :
        return False
    elif minute > set.mm and hour == set.hh:
        return False
    # elif second > set.ss :
    #     return False
    elif set.specific != 0:
        if set.specific == 1:
            for i in set.spe_list:
                if i == dayOfWeek:
                    return True
            return False
        elif set.specific == 2:
            for i in set.spe_list:
                if i == dayOfWeek:
                    return False
            return True
        pass
    else:
        return True


do_nothing = 0
shutdown_now = 1
shutdown_warn = 2
run_custom_cmd = 3

no_specific = 0
run_only_on = 1
run_except = 2