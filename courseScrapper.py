import bs4 as bs
import urllib.request

def course(s):
    
    string = '';
    
    sauce = urllib.request.urlopen('https://fas.calendar.utoronto.ca/search-courses?combine='+s).read()
    
    soup = bs.BeautifulSoup(sauce, 'lxml')
    
    
    count = 0
    for url in soup.find_all('a'):
        #print(url.text)
        if (url.text[0:6].lower() == s.lower()) and len(list(url.parent)) == 3:
            count+=1
           # print(url.text)
            string += url.text
            #print(list(url.parent))
            
    #print('huh')
    string += ' \n'
    
    temp = 0
    for text in soup.find_all('td',{'class':'views-field views-field-field-course-title'}):
        if temp == count:
            #print('ayooo')
            #print(text.text.strip())
            string += text.text.strip()      
            break
        temp+=1
        
    #print('huh')
    string += ' \n'

    temp = 0    
    for text in soup.find_all('td',{'class':'views-field views-field-body'}):
        #print(url.text)
        if temp == count:
            #print('ayooo')            
            #print(text.text.strip())
            string += text.text.strip()      
            
        temp+=1
        
    string += ' \n'
    
    temp = 0    
    for text in soup.find_all('td',{'class':'views-field views-field-field-prerequisite1'}):
        #print(url.text)
        if temp == count:
            #print('ayooo')            
            #print(text.text.strip())
            string += text.text.strip()                  
        temp+=1
    
    return string
