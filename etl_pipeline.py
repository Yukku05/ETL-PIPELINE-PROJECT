import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)
    print("Data extracted successfully.")
    return df

def transform_data(df):
    df = df.drop_duplicates()
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df = df[df['Order Date'].notnull()]
    df['Total Price'] = df['Quantity'] * df['Unit Price']
    print("Data transformed successfully.")
    return df

def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print("Data loaded successfully to output file.")

def run_etl():
    input_file = 'data/sales_data.csv'
    output_file = 'output/cleaned_sales_data.csv'

    raw_data = extract_data(input_file)
    clean_data = transform_data(raw_data)
    load_data(clean_data, output_file)

if __name__ == "__main__":
    run_etl()
