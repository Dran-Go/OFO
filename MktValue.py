def run_formula(dv):
    MktValue = dv.add_formula('MktValue',
                              "close*capital_stk",
                              is_quarterly=False, add_data=False)
    return MktValue