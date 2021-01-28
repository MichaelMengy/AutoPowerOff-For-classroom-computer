import time


class time_rule:

    """
    Class used for determining a shutdown rule

    ____________

    Args:

        enabled: bool whether the rule is enabled

        hh: int trigger hour

        mm: int trigger minute

        ss: int trigger second

        operation: int 0 = nothing | 1 = shutdown immeadiately | 2 = delayed shutdown

        specific rule: int 0 = no specific rule | 1 = the rule will be triggered only when DayOfWeek matches the ones in spe list | 2 = the rule should be triggered except the folowing days

        spe list: int list 
    """

    def __init__(self,enabled: bool,hh: int,mm: int,ss: int,operation: int,specific_rule: int,spe_list: list) -> None:
        self.enabled = enabled
        self.hh = hh
        self.mm = mm
        self.ss = ss
        self.operation = operation
        self.specific = specific_rule
        self.spe_list = spe_list
        pass
def check(hour:int,minute:int,second:int,dayOfWeek:int,set: time_rule) -> bool:
    '''
    Checks whether the rule will be executed
    '''
    errors = False
    if (set.hh > 24 or set.hh <0) or (set.mm >59 or set.mm < 0) or (set.ss > 59 or set.ss < 0):
        errors = True
        raise ValueError("Invalid time!")
        pass
    if (set.operation > 2 or set.operation < 0) or (set.specific > 2 or set.specific < 0):
        errors = True
        raise ValueError("Invalid operation or specific rule!")
    if (set.operation != 0 and len(set.spe_list) == 0):
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

no_specific = 0
run_only_on = 1
run_except = 2