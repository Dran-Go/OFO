def run_formula(dv):
    BIAS10 = dv.add_formula('BIAS10_J',
                            "(close/Ta('MA',0,open,high,low,close,volume,10)-1)*100",
                            is_quarterly=False, add_data=False)
    return BIAS10