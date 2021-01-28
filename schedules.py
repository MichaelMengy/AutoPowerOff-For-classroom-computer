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

    def __init__(self,enabled,hh,mm,ss,operation,specific_rule,spe_list) -> None:
        self.enabled = enabled
        self.hh = hh
        self.mm = mm
        self.ss = ss
        self.operation = operation
        self.specific = specific_rule
        self.spe_list = spe_list
        pass
def check(cur: time_rule,set: time_rule) -> bool:
    if cur.hh > set.hh :
        return False
    elif cur.mm > set.mm :
        return False
    elif cur.ss > set.ss :
        return False
    return True
    pass