#A9
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Hardcoded data
data = {
    'Age': [25, 30, 38, 45, 29, 60],
    'TSH': [1.2, 0.5, 0.3, 1.2, 6.5, 25.0]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# --- Min-Max Normalization ---
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df[['Age', 'TSH']])
df_minmax = pd.DataFrame(minmax_scaled, columns=['Age_MinMax', 'TSH_MinMax'])

# --- Z-Score Normalization ---
zscore_scaler = StandardScaler()
zscore_scaled = zscore_scaler.fit_transform(df[['Age', 'TSH']])
df_zscore = pd.DataFrame(zscore_scaled, columns=['Age_Zscore', 'TSH_Zscore'])

# Combine and show results
df_combined = pd.concat([df, df_minmax, df_zscore], axis=1)
print("\nNormalized Data:\n", df_combined)