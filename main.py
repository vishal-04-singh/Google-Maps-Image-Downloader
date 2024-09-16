from bs4 import BeautifulSoup
import urllib.request
import concurrent.futures


# Assuming you have the HTML in a file called "example.html"
with open('example.html',encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

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

# Outputting the JSON data to a file called "example.json"

    
destination = '/Users/vishal04/Desktop/Image_Download_from_Gmap_by_user/'
urls = []

for i in json_data['img']:
    line = i['src'].split('=')[0]+'=s0*#@' + i['src'].split('=')[0].split('/')[-1]+'.jpg'
    urls.append(line)


       
n=0
def main(url):
    global n
    try:
      urllib.request.urlretrieve(url.split('*#@')[0],destination+"\\"+url.split('*#@')[1])
    except:         
        try:
            urllib.request.urlretrieve(url.split('*#@')[0],destination+"\\"+url.split('*#@')[1])
        except Exception as e:      
            print(e)
    n+=1
    print(n)


def main2():
    # Run request concurrently.
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as Executor:
        # Local variable.
        # Load executor with url to fetch and work on.
        future_to_url = {Executor.submit(
            main, url=url): url for url in urls}
        # Loop over futures request and mark them completed.
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as e:
                # Raise exception.
                raise(e)
if __name__ == '__main__':
    main2()