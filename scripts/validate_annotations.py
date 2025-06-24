import pandas as pd

def validate_annotations(file_path):
    df = pd.read_csv(file_path)
    
    issues = []
    if 'Company_Name' not in df.columns or 'Product_Line' not in df.columns:
        issues.append("Missing required columns.")
    
    if df['Product_Line'].isnull().any():
        issues.append("Null values found in Product_Line column.")

    unique_labels = df['Product_Line'].nunique()
    print(f"Unique Product Lines: {unique_labels}")

    if issues:
        print("Validation Issues:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Validation passed. No issues found.")

# Example usage
if __name__ == "__main__":
    validate_annotations("../data/annotations_sample.csv")

