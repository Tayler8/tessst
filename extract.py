import pandas as pd
import random
import string

def generate_random_string(length=10):
    """Generate a random string of letters and digits."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def extract_data_from_excel(excel_file='news_data.xlsx'):
    try:
        # Load the Excel file into a DataFrame
        df = pd.read_excel(excel_file)

        # Check for missing values in 'Title' and 'Content' columns
        missing_title_indices = df[df['Title'].isnull()].index
        missing_content_indices = df[df['Content'].isnull()].index

        # Replace missing values with random strings
        for index in missing_title_indices:
            df.at[index, 'Title'] = generate_random_string()

        for index in missing_content_indices:
            df.at[index, 'Content'] = generate_random_string()

        # Display the content of the DataFrame
        print("Extracted Data:")
        print(df)

        # Access specific columns or rows as needed
        titles = df['Title'].tolist()
        contents = df['Content'].tolist()

        print("\nTitles:")
        print(titles)

        print("\nContents:")
        print(contents)

        return titles, contents

    except FileNotFoundError:
        print(f"Error: File '{excel_file}' not found.")
        return None, None

if __name__ == "__main__":
    extracted_titles, extracted_contents = extract_data_from_excel()

    # Now you can use the extracted data for further analysis or processing
    # For example, you could perform sentiment analysis as shown in the previous example
