def run_formula(dv):
    alpha136 = dv.add_formula("alpha136",
                              "((-1*Rank(Delay(Return(close,1,0), 3)))*Correlation(open, volume, 10))",
                              is_quarterly=False, add_data=False)
    return alpha136
