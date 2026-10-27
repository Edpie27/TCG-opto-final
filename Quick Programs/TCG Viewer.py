# Run this program if you ever need an overview of the TCG sales data, use data viewer for a cleaner layout.
import pandas as pd
tcg = pd.read_csv(r"C:\Program Files (x86)\Steam\steamapps\common\TCG Card Shop Simulator\BepInEx\config\ShopSense\Shops\Top-Pull\sales.csv")
print(tcg)