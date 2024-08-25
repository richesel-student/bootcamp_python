def split_booty(*args):
    gold_ingots_values = []

    for item in args:
        gold_ingots_values.append(item.get('gold_ingots', 0))
    gold_ingots_list = list(gold_ingots_values)
    lens = int(len(args))
    dicts = []
    golds_int = sum(gold_ingots_list)
    for i in range(len(args)):
        dicts.append({'gold_ingots': 0})

    for i in range(golds_int):
        dicts[i % lens]['gold_ingots'] += 1

    return dicts



