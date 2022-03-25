def extract_info(web_list):
    res=[]
    for i in range(len(web_list)):
        title=web_list[i].find("dt").find("a").text
        artist=web_list[i].find("dd",{"class":"desc"}).find("a").text
        stars=web_list[i].find("div",{"class":"rating_type"}).find("strong").text
            

        res.append({'title':title,
        'artist':artist,
        'stars':stars,})
    return res