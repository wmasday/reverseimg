import requests, re, string
from colorama import Fore, Style, Back
# import webbrowser

banner = """
  ,-""-.
 /--.   \  .-.-'`-~     \033[04mReverse Image\033[00m
| \033[91m()\033[00m )   |<_.-.    
 \--'   / `~._ `~'      \033[91m*\033[00m Author : keyw0rds
  `-..-'      `-        \033[91m*\033[00m Github : akuhidayat
  
"""

def reversimage():
    print (banner)
    fileName = input("["+ Fore.BLUE +"?"+ Style.RESET_ALL +"] Filename : ")
    apiUrl = 'http://www.google.com/searchbyimage/upload'
    data = {'encoded_image': (fileName, open(fileName, 'rb')), 'image_content': ''}
    postData = requests.post(apiUrl, files=data, allow_redirects=False)
    fetchUrl = postData.headers['Location']
    # webbrowser.open(fetchUrl)

    headers = {
      'user-agent':'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
      'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    num = 0;
    
    getUrl = requests.get(fetchUrl, headers=headers).content
    response = getUrl.decode('utf-8')
    searchResult = re.findall('<div class="r5a77d">(.*?)</div>', response)[0]
    hrefResult = re.findall('href="(.*?)"', response)
    findalResult = searchResult.replace("&nbsp;", " : ")
    print (Fore.BLUE +"\n |----[ "+ Fore.WHITE +"\033[04mreversimage"+ Fore.BLUE +"(c)"+ Fore.WHITE+ "akuhidayat\033[00m "+ Fore.BLUE +"]")
    print (" | "+ Fore.WHITE)
    print ("["+ Fore.BLUE +"!"+ Fore.WHITE +"]", findalResult)
    print (Fore.BLUE +" | ")
    print (Fore.WHITE +"["+ Fore.BLUE +"!"+ Fore.WHITE +"] Manual Url : ", fetchUrl)
    print (Fore.BLUE +" | ")
    for res in hrefResult:
        num += 1
        print (Fore.WHITE +"["+ Fore.BLUE, num, Fore.WHITE +"] Links Result : ", res)
    
reversimage()