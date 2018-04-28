def run_formula(dv):
    def sma(df, n, m):
        a = n / m - 1
        r = df.ewm(com=a, axis=0, adjust=False)
        return r.mean()

    alpha122 = dv.add_formula("alpha122",
                              "(SMA(SMA(SMA(Log(close),13,2),13,2),13,2)-Delay(SMA(SMA(SMA(Log(close),13,2),13,2),13,2),1))/Delay(SMA(SMA(SMA(Log(close),13,2),13,2),13,2),1)",
                              is_quarterly=False, add_data=False,
                              register_funcs={"SMA": sma})

    return alpha122