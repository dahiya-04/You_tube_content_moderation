
#YouTube Comment Scraper
This Python script allows you to search for YouTube videos based on specific criteria and extract comments from those videos. It utilizes the YouTube Data API to perform searches and retrieve comments.

Features
Search for YouTube videos using keywords and category IDs

Extract comments from the searched videos

Save video details and comments to a CSV file

Prerequisites
Before running the script, make sure you have the following:

Python 3.x installed on your system

A Google Cloud project with the YouTube Data API enabled

An API key for accessing the YouTube Data API

Installation
Clone this repository or download the script file.

Install the required Python packages:

bash
pip install google-api-python-client python-dotenv
Create a .env file in the same directory as the script and add your YouTube Data API key:

text
API_KEY=your_api_key_here
Usage
To use the script, follow these steps:

Open the script in a Python editor or IDE.

Modify the search parameters in the if __name__ == '__main__': section:

python
search_videos('search_query', 'category_id', max_results=number_of_videos, output_file='output_filename.csv')
search_query: Keywords to search for (e.g., 'explicit lyrics|adult content|nsfw')

category_id: YouTube video category ID (e.g., '24' for Entertainment, '27' for Education)

max_results: Maximum number of videos to fetch (default is 10)

output_file: Name of the CSV file to save the results (default is 'videos_with_comments.csv')

Run the script:

bash
python script_name.py
Functions
get_all_comments(video_id)
This function fetches all comments from a specific YouTube video.

search_videos(query, category_id, max_results=10, output_file='videos_with_comments.csv')
This function searches for YouTube videos based on the provided query and category, then extracts comments from those videos and saves the results to a CSV file.

Output
The script generates a CSV file with the following columns:

VideoID

Title

Description

Comment

Each row represents a single comment, along with the details of the video it belongs to.

Limitations
The script is subject to YouTube API quotas and limits.

The number of comments retrieved may be limited by API restrictions.

Legal Considerations
Ensure that you comply with YouTube's terms of service and API usage guidelines when using this script. Respect copyright and privacy laws when collecting and using data from YouTube.

Disclaimer
This script is for educational purposes only. The user is responsible for any consequences of using this script and should ensure they have the necessary permissions and rights to collect and use YouTube data.
