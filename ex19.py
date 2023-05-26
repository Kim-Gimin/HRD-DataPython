import pandas as pd
month_se = pd.Series(['1월', '2월', '3월', '4월'])
income_se = pd.Series([9_500, 6_200, 6_050, 7_000])
expense_se = pd.Series([5_040, 2_350, 2_300, 4_800])
df = pd.DataFrame({'월':month_se, '수입':income_se, '지출':expense_se })
print(df)
import numpy as np
print(np.argmax(income_se))
print(month_se[0])