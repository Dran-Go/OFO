# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈南浩" # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    乖离率（10-day Bias Ratio/BIAS），简称Y值，是移动平均原理派生的一项技术指标，表示股价偏离趋势指标斩百分比值。
    """
    name = "BIAS10" # 和文件名即因子名一致
    value = dv.add_formula(name, "(close/Ta('MA',0,open,high,low,close,volume,10)-1)*100",
                           is_quarterly=False, add_data=True)
    return value
