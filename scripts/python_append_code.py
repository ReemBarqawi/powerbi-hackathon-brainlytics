import pandas as pd

# Load CSVs with encoding fix + skip bad lines
df1 = pd.read_csv("BrainLyticsData1.csv", encoding="latin1", on_bad_lines="skip")
df2 = pd.read_csv("BrainLyticsData2.csv", encoding="latin1", on_bad_lines="skip")

print("Shape of File 1:", df1.shape)
print("Shape of File 2:", df2.shape)

# Clean column names
df1.columns = df1.columns.str.strip().str.replace(" ", "_").str.lower()
df2.columns = df2.columns.str.strip().str.replace(" ", "_").str.lower()

# Append datasets
combined_df = pd.concat([df1, df2], ignore_index=True)

print("Combined Shape:", combined_df.shape)

# Drop duplicates
combined_df = combined_df.drop_duplicates()

# Export final file
combined_df.to_csv("BrainLytics_Final.csv", index=False, encoding="utf-8")

print("Final dataset exported as BrainLytics_Final.csv")
