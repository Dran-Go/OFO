def run_formula(dv):
    AD20 = dv.add_formula('AD20_J',
                          "Ta('MA',0,0,0,0,Ta('AD',0,0,high,low,close,volume),0,20)",
                          is_quarterly=False, add_data=True)
    return AD20