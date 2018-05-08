# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈南浩" # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    长期借款与资产总计之比（Long term loan to total assets）
    计算方法：LongDebtToAsset=长期借款/总资产
    """
    name = "LongDebtToAsset" # 和文件名即因子名一致
    value = dv.add_formula(name, "lt_borrow/tot_assets",
                           is_quarterly=False, add_data=True)
    return value
