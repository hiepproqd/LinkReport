import requests
import json




api_url = 'https://api.worksheetzone.org/api/get-all-short-links'
todo = {"tags":[],"country":""}
response = requests.post(api_url, json=todo)
links = response.json()



def check_func():
    pass_link_count = 0
    down_link_count = 0
    link_down_list = "LINKS DOWN:"

    for link in links:
        short_link = "https://wsz.app/" + link['shortLink'] 
        original_link = link['originalLink']
    
        x = requests.get(short_link)
    
    
        if original_link == x.url and x.status_code == 200 :
            pass_link_count += 1
        
       
        else:
            link_down =  f'link down: {original_link}'
            down_link_count += 1
            link_down_list = link_down_list + '\n\n' + original_link
            with open('linkdown.txt', 'w') as ld:
                ld.write(link_down_list)
    
    
            
 
    if down_link_count == 0:
        pass       
    elif pass_link_count == 0:
        return 'ALL LINK DOWN! SHORTLINKS SYSTEM ERROR'
    else:
        return '!!SOME LINKS GET ERROR!!'



    




