import pandas as pd

def remove_duplicates(file_path):
    """
    Removes duplicate rows from a CSV file and saves the cleaned data.
    
    :param file_path: Path to the CSV file to clean.
    """
    df = pd.read_csv(file_path)
    
    # Remove duplicates
    initial_count = df.shape[0]
    df.drop_duplicates(inplace=True)
    final_count = df.shape[0]
    
    # Save changes back to the file
    df.to_csv(file_path, index=False)
    
    if initial_count != final_count:
        print(f"Removed {initial_count - final_count} duplicate rows.")
    else:
        print("No duplicates found.")
