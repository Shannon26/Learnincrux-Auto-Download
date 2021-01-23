import requests
from pathlib import Path
from bs4 import BeautifulSoup

URL = 'https://www.learningcrux.com/course/learn-c-programming-beginner-to-advance-deep-dive-in-c'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='content')

job_elems = results.find_all('section', class_='sectionRow')

for job_elem in job_elems:
  for h2 in job_elem.find_all('h2'):
    sectionHead = h2.text
    sectionHead = sectionHead.replace('\n', ' ')
    sectionHead = sectionHead.replace(" ", "")
    Path("/content/gdrive/Shared drives/Manchester/Learn/"+sectionHead).mkdir(parents=True, exist_ok=True)
    pathname ="/content/gdrive/Shared drives/Manchester/Learn/"+sectionHead
    pathname = pathname+"/"

  for a in job_elem.find_all('a', href=True):
    # Name Of File
    heading = a.text
    heading = heading.replace('\n', ' ')
    heading = heading.split('Video', 1)[0]
    
    # URL Link
    linkurl = "https://www.learningcrux.com",a['href']
    url1 =  ''.join(linkurl)
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    job_elems1 = soup1.find_all('source')
    for a in job_elems1:
      linkurl1 = "https://www.learningcrux.com",a['src']
      str2 =  ''.join(linkurl1)

      #Download to Drive
      file_url = str2
      Name1 = heading + ".mp4"
      r = requests.get(file_url, stream = True)
      with open(pathname +Name1, "wb") as file:
        for block in r.iter_content(chunk_size = 1024):
          if block:
            file.write(block)
