# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈南浩" # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    20日累积/派发线（20-days Accumulation/Distribution Line）
    该指标将每日的成交量通过价格加权累计，用以计算成交量的动量。
    """
    name = "AD20" # 和文件名即因子名一致
    value = dv.add_formula(name, "Ta('MA',0,0,0,0,Ta('AD',0,0,high,low,close,volume),0,20)",
                           is_quarterly=False, add_data=True)
    return value
