# Google Maps Image Downloader

This Python script downloads high-resolution images from Google Maps based on HTML content containing image tags from user-uploaded photos in reviews.

## Important Disclaimer

This tool is intended for educational purposes only. Do not use it for any malicious or unethical purposes. Respect user privacy, copyright laws, and Google's terms of service. The authors and contributors are not responsible for any misuse of this tool.

## Files

- `Main.py`: The main script that handles the image downloading process.
- `Example.html`: An HTML file containing img tags with Google Maps image URLs.

## Features

- Extracts image URLs from an HTML file
- Downloads high-resolution images from Google Maps user-uploaded photos
- Fast and efficient downloading process

## Requirements

- Python 3.x
- Required Python libraries (list them here, e.g., requests, BeautifulSoup4)

## Usage

1. Ensure you have the required Python libraries installed:
   ```
   pip install -r requirements.txt
   ```

2. Obtain the HTML content for `Example.html`:
   a. Go to Google Maps and search for a famous place.
   b. Navigate to the review section of the place.
   c. Find a user who has uploaded multiple images and click on their profile.
   d. In the user's profile, go to the photo section.
   e. Scroll down to the bottom of the page.
   f. Right-click on the scroll bar and select "Inspect" to open the developer tools.
   g. Press F2 on your keyboard to edit the HTML section.
   h. Copy the relevant HTML content containing the img tags.
   i. Paste this content into a new file named `Example.html` in the same directory as the script.

3. Run the script:
   ```
   python main.py
   ```

4. The script will process the HTML file, extract image URLs, and download the high-resolution images to the current directory.

## How It Works

The script reads the `Example.html` file, which contains img tags from Google Maps user-uploaded photos. It extracts the image URLs from these tags and then downloads the corresponding high-resolution images.

## Ethical Use and Legal Considerations

- This tool is for educational and research purposes only.
- Do not use this tool to violate privacy or copyright laws.
- Obtain proper permissions before downloading or using images.
- Respect Google's terms of service and the rights of content creators.
- Do not use the downloaded images for commercial purposes without proper authorization.
- Be aware of and comply with local and international laws regarding web scraping and data collection.

## Troubleshooting

If you encounter issues with extracting the correct HTML content:
- Make sure you've scrolled to the bottom of the user's photo section to load all images.
- Verify that the copied HTML contains the necessary img tags with the image URLs.
- Check that the `Example.html` file is properly formatted and saved in the correct location.

## Contributing

Feel free to fork this project and submit pull requests with any enhancements. Please ensure that any contributions adhere to the ethical guidelines outlined in this README.
