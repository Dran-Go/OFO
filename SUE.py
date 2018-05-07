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
        if int(i/10000)<(int(df2.index[0]/10000)+4) :    # 小于五年，取全部
            sue.loc[i] = (df2.loc[i] - df2.loc[:i].drop(i).mean())/df2.loc[:i].drop(i).std()
        else:                                            # 取最近五年
            sue.loc[i] = (df2.loc[i] - df2.loc[:i].iloc[-5:].drop(i).mean())/df2.loc[:i].iloc[-5:].drop(i).std()
    for i in df_day.index:
        if i in sue.index:
            df_day.loc[i] = sue.loc[i]
        else:
            df_day.loc[i] = np.NaN
    df_day = df_day.fillna(method='ffill')
    return df_day



def run_formula(dv):
    SUE = dv.add_formula("SUE_J", "SUE(NP2Y(net_profit),close)",
                         is_quarterly=False,
                         add_data=True,
                         register_funcs={"NP2Y": net_profit_to_year, "SUE": sue})
    return SUE