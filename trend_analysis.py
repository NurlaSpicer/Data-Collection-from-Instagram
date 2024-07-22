import pandas as pd
import matplotlib.pyplot as plt

def plot_media_trends(df):
    """
    Plots media post trends by month.
    
    :param df: DataFrame with media data
    """
    try:
        # Group data by month and count number of posts
        df.groupby(df['timestamp'].dt.to_period('M')).size().plot(kind='bar')
        plt.title('Monthly Media Posts')
        plt.xlabel('Month')
        plt.ylabel('Number of Posts')
        plt.show()
    except Exception as e:
        print(f"Error creating plot: {e}")

if __name__ == "__main__":
    data = {
        'data': [
            {'id': '1', 'timestamp': '2024-07-22T12:34:56Z'},
            {'id': '2', 'timestamp': '2024-07-15T12:34:56Z'},
            # Add more sample data as needed
        ]
    }
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    plot_media_trends(df)
