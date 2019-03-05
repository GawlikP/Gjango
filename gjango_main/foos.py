def return_values_from_stats(*values):
    a = []
    for v in values:
        if v[4:] == '': a.append('0')
        else: a.append(v[4:])
    results = [int(i) for i in a]
    return results;
