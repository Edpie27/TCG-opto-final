# Run this program if you need to retrive any product keys. Using data viewer is recommended

import pandas as pd
tcg = pd.read_csv(r"C:\Program Files (x86)\Steam\steamapps\common\TCG Card Shop Simulator\BepInEx\config\ShopSense\Shops\Top-Pull\sales.csv")
keys = tcg.loc[:,['key','name']]
keys.set_index("key")
keys.drop_duplicates(inplace = True)
print(keys)