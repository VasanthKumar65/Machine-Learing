#A8
import numpy as np
import pandas as pd
from scipy.stats import mode

# --- Sample dataset with missing values ---
data = {
    'Age': [25, 30, np.nan, 45, 29, 60],
    'TSH': [1.2, 0.5, 0.3, np.nan, 6.5, 25.0],
    'Sex': ['F', 'M', 'F', np.nan, 'F', 'M'],
    'On_thyroxine': ['no', 'yes', 'no', 'no', np.nan, 'yes']
}

df = pd.DataFrame(data)
print("Before Imputation:\n", df)
# 1. Age: numeric without major outliers → mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# 2. TSH: numeric with outliers → median
df['TSH'].fillna(df['TSH'].median(), inplace=True)

# 3. Sex: categorical → mode
df['Sex'].fillna(df['Sex'].mode()[0], inplace=True)

# 4. On_thyroxine: categorical → mode
df['On_thyroxine'].fillna(df['On_thyroxine'].mode()[0], inplace=True)

print("\nAfter Imputation:\n", df)