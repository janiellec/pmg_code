import subprocess
from pathlib import Path
import pandas as pd


def test_combiner_main():
    """ Tests that combiner.py functions well
    """
    subprocess.run(["python3", "generatefixtures.py"])

    PATHS = ['fixtures/accessories.csv', 'fixtures/clothing.csv', 'fixtures/household_cleaners.csv']
    lengths = []
    for p in PATHS:
        assert Path(p).exists()
        temp = pd.read_csv(p, quotechar='"', escapechar="\\")
        # add length of file
        lengths.append(len(temp) - 1)

    with open("temp.csv", "w+") as temp:
        print("Testing input combinations")
        
        for indx in range(3):
            subprocess.run(["python3", "combiner.py", "./" + PATHS[indx]], 
                            stdout=temp)

            out = len(pd.read_csv('temp.csv')) - 1
            assert out == lengths[indx]
            temp.truncate(0)

        for indx in range(3):
            subprocess.run(["python3", "combiner.py", "./" + PATHS[indx], "./" + PATHS[(indx + 1) % 3]], 
                            stdout=temp)

            out = len(pd.read_csv('temp.csv')) - 2
            assert out == lengths[indx] + lengths[(indx + 1) % 3]

            if indx != 2:
                temp.truncate(0)







    

