# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈南浩" # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    alpha136公式：((-1 * RANK(DELTA(RET, 3))) * CORR(OPEN, VOLUME, 10))
    """
    name = "alpha136" # 和文件名即因子名一致
    value = dv.add_formula(name, "((-1*Rank(Delay(Return(close,1,0), 3)))*Correlation(open, volume, 10))",
                           is_quarterly=False, add_data=True)
    return value
