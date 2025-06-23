# Google Maps Image Downloader

A Python script to extract and download images from Google Maps HTML content with concurrent processing for faster downloads.

## 🚀 Features

- **HTML Parsing**: Extracts image URLs from Google Maps HTML files
- **Concurrent Downloads**: Uses ThreadPoolExecutor for fast parallel downloads
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Error Handling**: Robust error handling with retry mechanisms
- **Progress Tracking**: Real-time download progress monitoring
- **File Safety**: Automatic filename sanitization and duplicate checking

## 📋 Prerequisites

- Python 3.6 or higher
- Required Python packages (see [Installation](#installation))

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vishal-04-singh/Google-Maps-Image-Downloader.git
   cd Google-Maps-Image-Downloader
   ```

2. **Install required packages:**
   ```bash
   pip install beautifulsoup4 requests
   ```

   Or install from requirements file:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Basic Usage

1. **Prepare your HTML file:**
   - Save your Google Maps HTML content as `example.html` in the project directory
   - The HTML should contain `<img>` tags with Google Maps image URLs

2. **Update the destination path:**
   ```python
   destination = '/path/to/your/download/folder/'
   ```

3. **Run the script:**
   ```bash
   python image_downloader.py
   ```

### Example

```python
from bs4 import BeautifulSoup
import urllib.request
import concurrent.futures
import os

# Your HTML file containing Google Maps images
with open('example.html', encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# Set your download destination
destination = '/Users/username/Downloads/google_maps_images/'

# Run the downloader
# The script will automatically extract and download all images
```

## 🏗️ Project Structure

```
Google-Maps-Image-Downloader/
│
├── image_downloader.py          # Main script (original version)
├── fixed_image_downloader.py    # Fixed version with better error handling
├── enhanced_version.py          # Enhanced version with requests library
├── example.html                 # Sample HTML file (you provide this)
├── requirements.txt             # Python dependencies
└── README.md                   # This file
```

## 🔧 Configuration

### Download Settings

- **Max Workers**: Adjust the number of concurrent downloads
  ```python
  max_workers=10  # Recommended: 5-10 for stability
  ```

- **Destination Path**: Set your preferred download location
  ```python
  destination = '/your/preferred/path/'
  ```

- **Image Quality**: Modify URL parameters for different image sizes
  ```python
  line = i['src'].split('=')[0] + '=s0'  # s0 = original size
  ```

## 🚨 Common Issues & Solutions

### Issue 1: File Path Errors
```
[Errno 2] No such file or directory
```
**Solution**: Ensure the destination directory exists and use proper path separators.

### Issue 2: Download Failures
**Solution**: The script includes automatic retry mechanisms and better error handling in the enhanced version.

### Issue 3: HTML File Not Found
**Solution**: Make sure `example.html` is in the same directory as the script.

## 📝 Code Versions

### 1. Original Version (`image_downloader.py`)
- Basic functionality with backslash path issues

### 2. Fixed Version (`fixed_image_downloader.py`)
- ✅ Cross-platform path handling
- ✅ Directory creation
- ✅ Better error handling
- ✅ Progress tracking

### 3. Enhanced Version (`enhanced_version.py`)
- ✅ Uses `requests` library for better HTTP handling
- ✅ Session management for connection reuse
- ✅ File existence checking
- ✅ User-Agent headers
- ✅ Rate limiting
- ✅ Success/failure statistics

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

- This tool is for educational purposes
- Respect Google's Terms of Service and rate limits
- Ensure you have permission to download the images
- The script includes respectful delays to avoid overwhelming servers

## 🐛 Known Issues

- Large concurrent downloads may be rate-limited
- Some Google Maps URLs may require authentication
- Filename sanitization may alter original names

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/vishal-04-singh/Google-Maps-Image-Downloader/issues) section
2. Create a new issue with detailed information
3. Contact: [Your Contact Information]

## 🙏 Acknowledgments

- BeautifulSoup4 for HTML parsing
- Python's concurrent.futures for parallel processing
- Google Maps for the image source

---

**Star ⭐ this repository if you found it helpful!**