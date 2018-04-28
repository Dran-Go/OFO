def run_formula(dv):
    LongDebtToAsset = dv.add_formula('LongDebtToAsset',
                                     "lt_borrow/tot_assets",
                                     is_quarterly=False, add_data=False)
    return LongDebtToAsset
