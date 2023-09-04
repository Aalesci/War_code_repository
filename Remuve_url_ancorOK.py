#Complete the function/method so that it returns the url with anything after the anchor (#) removed.

#Examples
#"www.codewars.com#about" --> "www.codewars.com"
#"www.codewars.com?page=1" -->"www.codewars.com?page=1"


def remove_url_anchor(url):
    cont = 0
    output = url
    for d in url:
        if d != '#': 
            cont += 1
        else: 
            output = url[:cont] 
            break
    return output 


url = 'www.codewars.com/katas/#'

print(remove_url_anchor(url))



#Better oprion: 
#def remove_url_anchor(url):
#  return url.split('#')[0]