import re
from logging import config, getLogger

from myproject.public import logs_add
config.dictConfig(logs_add.LOGGING_DIC)
log = getLogger("logs")

def comper_str(expect, actual):
    # exp = str.replace(str(expect), '*', "([\\s\\S]*)")
    # exp = exp.replace("(", "\\(")
    # exp = exp.replace(")", "\\)")
    if re.match(str(expect), str(actual)):
        log.info(str(expect)+"---"+str(actual)+"结果一致")
    else:
        log.info(str(expect)+"---"+str(actual)+"结果不一致")
        assert False


def comper_json(expect, actual):
    assert isinstance(expect, dict)
    assert isinstance(actual, dict)
    for k, v in expect.items():
        if k not in actual.keys():
            return
        elif isinstance(v, dict):
            comper_json(v, actual[k])
        elif isinstance(v, list):
            comper_list(v, actual[k])
        else:
            comper_str(v, actual[k])
    for k,v in actual.items():
        if k not in expect.keys():
            return

def comper_list(expect, actual):
    assert isinstance(expect, list)
    assert isinstance(actual, list)
    i = 0
    is_succ = False
    for e in expect:
        i += 1
        # log.info(e)
        j = 0
        for a in actual:
            j += 1
            if i == j :
                if isinstance(e, dict):
                    comper_json(e, a)
                if isinstance(e, list):
                    comper_list(e, a)
                else:
                    comper_str(e, a)
        #         is_succ = True
        #     break
        # break
    # assert is_succ

