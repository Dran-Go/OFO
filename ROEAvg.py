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


def run_formula(dv):
    ROEAvg = dv.add_formula("ROEAvg",
                            "NPY(net_profit)*2/(EH(tot_shrhldr_eqy_excl_min_int)+EL(tot_shrhldr_eqy_excl_min_int))*100",
                            is_quarterly=True,
                            add_data=True,
                            register_funcs={"NPY": net_profit_year, "EH": eqy_head, "EL": eqy_last})
    return ROEAvg