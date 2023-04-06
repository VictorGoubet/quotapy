import pandas as pd

def test():
    helloworld = pd.Series(["hello", "world"])
    helloworld = pd.DataFrame(helloworld)
    print(helloworld)
