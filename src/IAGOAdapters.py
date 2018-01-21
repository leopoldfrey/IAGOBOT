# -*- coding: utf-8 -*-
# from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from datetime import datetime


def frenchMonths(month):
    result = ""
    if month == 1:
        result = "Janvier"
    elif month == 2:
        result = "Février"
    elif month == 3:
        result = "Mars"
    elif month == 4:
        result = "Avril"
    elif month == 5:
        result = "Mai"
    elif month == 6:
        result = "Juin"
    elif month == 7:
        result = "Juillet"
    elif month == 8:
        result = "Aout"
    elif month == 9:
        result = "Septembre"
    elif month == 10:
        result = "Octobre"
    elif month == 11:
        result = "Novembre"
    elif month == 12:
        result = "Décembre"
    else:
        result = "Date inconnue"
    return result


class HeureAdapter(LogicAdapter):

    def __init__(self, **kwargs):
        super(HeureAdapter, self).__init__(**kwargs)
    
    def can_process(self, statement):
        words = ['heure', 'date', 'maintenant']
        if any(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        # import random
        confidence = 1
        t1 = datetime.now()
        selected_statement = Statement("Nous sommes le %s %s %s, et il est %s:%s" % (t1.day, frenchMonths(t1.month), t1.year, t1.hour, t1.minute))
        selected_statement.confidence = confidence
        
        return selected_statement
