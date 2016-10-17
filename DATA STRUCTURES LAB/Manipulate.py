def manipulate_data(data):
    if isinstance(data, list):
        return [sum(1 for n in data if isinstance(n, int) and n >= 0), sum(n for n in data if isinstance(n, int) and n < 0)]
    else:
        return 'Only lists allowed'