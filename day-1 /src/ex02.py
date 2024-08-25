import ex01, ex00
def decorator(*func):
    def wrapper(*args):
        return f"SQUEAK{func}"
    return wrapper


@decorator
def add_ingot(purse):
    add_purse = purse.copy()
    if(add_purse is None or "gold_ingots" not in add_purse):
        return {}
    else:
        add_purse["gold_ingots"]+=1
        return add_purse

@decorator
def empty(purse):
  return {}


@decorator
def get_ingot(purse):
    if "gold_ingots" not in purse or purse["gold_ingots"] == 1:
        return {}
    return {"gold_ingots": purse["gold_ingots"] - 1}


@decorator
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










