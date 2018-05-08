# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈南浩" # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}


def sma(df, n, m):
    a = n / m - 1
    r = df.ewm(com=a, axis=0, adjust=False)
    return r.mean()

def run_formula(dv, params=default_params):
    """
    alpha122公式：(SMA(SMA(SMA(Log(close),13,2),13,2),13,2)-Delay(SMA(SMA(SMA(Log(close),13,2),13,2),13,2),1))/Delay(SMA(SMA(SMA(Log(close),13,2),13,2),13,2),1)
    """
    name = "alpha122" # 和文件名即因子名一致
    value = dv.add_formula(name,
                           "(SMA(SMA(SMA(Log(close),13,2),13,2),13,2)-Delay(SMA(SMA(SMA(Log(close),13,2),13,2),13,2),1))/Delay(SMA(SMA(SMA(Log(close),13,2),13,2),13,2),1)",
                           is_quarterly=False, add_data=True,
                           register_funcs={"SMA": sma})
    return value
