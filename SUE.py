# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "陈南浩" # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

import numpy as np

def net_profit_to_year(df):
    df2 = df.copy()
#     df2 = df.copy().fillna(method='ffill')   # 净利润net_profit部分数据缺失，进行向后填充
    netProfit = df2.copy()
    for i in netProfit.index[1:]:
        netProfit.drop(i, inplace=True)
    for i in df.index[1:]:
        year = int(i/10000)
        year_df = int(netProfit.index[-1]/10000)
        if year == year_df :
            netProfit.iloc[-1] = netProfit.iloc[-1] + df2.loc[i]
        else:
            netProfit = netProfit.append(df.loc[i])
    return netProfit

def sue(df, close):
    df2 = df.copy()
    df_day = close.copy()
    for i in df2.index:                     # 将不满一年的净利润数据删除
        if(int(str(i)[4:6])!=3):
            df2.drop(i, inplace=True)
    sue = df2.copy()
    for i in sue.index[0:2]:
        sue.drop(i, inplace=True)
    for i in sue.index :
        if int(i/10000)<(int(df2.index[0]/10000)+4) :    # 小于等于五年，取全部
            sue.loc[i] = (df2.loc[i] - df2.loc[:i].drop(i).mean())/df2.loc[:i].drop(i).std()
        else:                                            # 大于五年，取最近五年
            sue.loc[i] = (df2.loc[i] - df2.loc[:i].iloc[-5:].drop(i).mean())/df2.loc[:i].iloc[-5:].drop(i).std()
    for i in df_day.index:
        if i in sue.index:
            df_day.loc[i] = sue.loc[i]
        else:
            df_day.loc[i] = np.NaN
    df_day = df_day.fillna(method='ffill')
    return df_day

def run_formula(dv, params=default_params):
    """
    未预期盈余（Standardized unexpected earnings）
    计算方法：SUE=（最近一年净利润-除去最近一年的过往净利润均值）/除去最近一年的过往净利润标准差
    备注：过往净利润记录数大于五年时取最近五年的数据，记录数不足五年时取全部数据，最后结果只保留记录数不小于三年的数据
    """
    name = "SUE" # 和文件名即因子名一致
    value = dv.add_formula(name, "SUE(NP2Y(net_profit),close)",
                           is_quarterly=False, add_data=True,
                           register_funcs={"NP2Y": net_profit_to_year, "SUE": sue})
    return value
