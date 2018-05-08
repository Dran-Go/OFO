# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈南浩" # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

from datetime import datetime

def int2datetime(df):
    df2 = df.copy()
    date = []
    for i in df2.index:
        date.append(datetime.strptime(str(i), "%Y%m%d"))
    df2['datetime'] = date
    df2.set_index('datetime', drop=True, inplace=True)
    return df2

def datetime2int(df):
    df2 = df.copy()
    date = []
    for i in df2.index:
        date.append(int(i.strftime("%Y%m%d")))
    df2['trade_date'] = date
    df2.set_index('trade_date', drop=True, inplace=True)
    return df2

def net_profit_year(df):
    df2 = df.copy()
    return datetime2int(int2datetime(df2).resample('A').sum())

def eqy_head(df):
    df2 = df.copy()
    return datetime2int(int2datetime(df2).resample('A').head())

def eqy_last(df):
    df2 = df.copy()
    return datetime2int(int2datetime(df2).resample('A').last())

def run_formula(dv, params=default_params):
    """
    净资产收益率（平均）
    计算方法：REOAvg=归属于母公司的净利润*2(期末归属于母公司的所有者权益+期初归属于母公司的所有者权益)*100%
    """
    name = "ROEAvg" # 和文件名即因子名一致
    value = dv.add_formula(name, "NPY(net_profit)*2/(EH(tot_shrhldr_eqy_excl_min_int)+EL(tot_shrhldr_eqy_excl_min_int))*100",
                           is_quarterly=True, add_data=True,
                           register_funcs={"NPY": net_profit_year, "EH": eqy_head, "EL": eqy_last})
    return value
