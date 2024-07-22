import pandas as pd

def clean_media_data(data):
    """
    Cleans and prepares media data for analysis.
    
    :param data: Raw JSON response from the API
    :return: DataFrame with cleaned data
    """
    try:
        # Convert JSON to DataFrame
        df = pd.json_normalize(data['data'])
        # Convert 'timestamp' column to datetime format
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except KeyError as e:
        print(f"Data error: missing key {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error processing data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    media_data = {
        'data': [
            {'id': '1', 'caption': 'Sample post', 'timestamp': '2024-07-22T12:34:56Z'},
            # Add more sample data as needed
        ]
    }
    df = clean_media_data(media_data)
    print(df)
