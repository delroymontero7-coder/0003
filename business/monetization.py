def estimate_mode_cost(mode='normal'):
    table = {'barato': '$0-$10', 'normal': '$10-$50', 'monstruo': '$50-$200+'}
    return table.get(mode, table['normal'])
