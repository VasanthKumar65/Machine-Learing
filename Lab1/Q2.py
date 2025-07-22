# A2
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

records = {
    'Candy_Count': [20, 16, 27, 19, 24, 22, 15, 18, 21, 16],
    'Mango_Kgs': [6, 3, 6, 1, 4, 1, 4, 4, 1, 2],
    'Milk_Packets': [2, 6, 2, 2, 2, 5, 2, 2, 4, 4],
    'Total_Paid': [386, 289, 393, 110, 280, 167, 271, 274, 148, 198]
}

df2 = pd.DataFrame(records)
df2['Class'] = ['RICH' if amt > 200 else 'POOR' for amt in df2['Total_Paid']]
features = df2[['Candy_Count', 'Mango_Kgs', 'Milk_Packets']].values
targets = np.array([1 if lbl == 'RICH' else 0 for lbl in df2['Class']])

clf = LogisticRegression()
clf.fit(features, targets)
preds = clf.predict(features)
acc = accuracy_score(targets, preds)

print("Classification Report")
print(classification_report(targets, preds, target_names=['POOR', 'RICH']))
print(f"Accuracy: {acc:.2f}")

df2['Prediction'] = ['RICH' if p == 1 else 'POOR' for p in preds]
print("\nCustomer Classification")
print(df2[['Candy_Count', 'Mango_Kgs', 'Milk_Packets', 'Total_Paid', 'Class', 'Prediction']])