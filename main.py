from bs4 import BeautifulSoup
import urllib.request
import concurrent.futures
import os
import json

# Assuming you have the HTML in a file called "example.html"
try:
    with open('example.html', encoding='utf-8') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
except FileNotFoundError:
    print("Error: 'example.html' file not found. Please make sure the file exists.")
    exit(1)

# Converting the HTML to JSON
json_data = {}
for tag in soup.find_all(True):
    tag_name = tag.name
    if tag.attrs:
        tag_attrs = {}
        for attr, value in tag.attrs.items():
            tag_attrs[attr] = value
        if tag_name in json_data:
            json_data[tag_name].append(tag_attrs)
        else:
            json_data[tag_name] = [tag_attrs]
    else:
        if tag_name in json_data:
            json_data[tag_name].append(tag.string)
        else:
            json_data[tag_name] = [tag.string]

# Create destination directory if it doesn't exist
destination = '/Users/vishal04/Developer/Google-Maps-Image-Downloader/images'
os.makedirs(destination, exist_ok=True)

urls = []

# Check if 'img' key exists in json_data
if 'img' not in json_data:
    print("No 'img' tags found in the HTML file.")
    exit(1)

for i in json_data['img']:
    if 'src' in i and i['src']:  # Check if src attribute exists and is not empty
        try:
            line = i['src'].split('=')[0] + '=s0*#@' + i['src'].split('=')[0].split('/')[-1] + '.jpg'
            urls.append(line)
        except IndexError:
            print(f"Skipping malformed URL: {i['src']}")
            continue

n = 0

def main(url):
    global n
    try:
        # Use os.path.join for proper path construction
        filename = url.split('*#@')[1]
        # Sanitize filename to remove invalid characters
        filename = "".join(c for c in filename if c.isalnum() or c in ('-', '_', '.')).rstrip()
        filepath = os.path.join(destination, filename)
        
        urllib.request.urlretrieve(url.split('*#@')[0], filepath)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {url.split('*#@')[1] if '*#@' in url else url}: {e}")
    
    n += 1
    print(f"Progress: {n}/{len(urls)}")

def main2():
    if not urls:
        print("No URLs to download.")
        return
    
    print(f"Starting download of {len(urls)} images...")
    
    # Run requests concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:  # Reduced workers to be more respectful
        # Load executor with urls to fetch
        future_to_url = {executor.submit(main, url=url): url for url in urls}
        
        # Loop over futures and handle completion
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as e:
                print(f"Exception occurred for {url}: {e}")

if __name__ == '__main__':
    main2()
    print("Download process completed!")