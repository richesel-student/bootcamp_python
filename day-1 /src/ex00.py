def add_ingot(purse):
    add_purse = purse.copy()
    if(add_purse is None or "gold_ingots" not in add_purse):
        return {}
    else:
        add_purse["gold_ingots"]+=1
        return add_purse

def empty(purse):
  return {}

def get_ingot(purse):
    if "gold_ingots" not in purse or purse["gold_ingots"] == 1:
        return {}
    return {"gold_ingots": purse["gold_ingots"] - 1}




