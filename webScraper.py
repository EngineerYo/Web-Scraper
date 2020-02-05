import requests

from PIL import Image
from bs4 import BeautifulSoup as bs4

urlStub = 'https://en.wikipedia.org/wiki/'
senators = ['Tammy Baldwin', 'Michael Bennet', 'Richard Blumenthal', 'Cory Booker', 'Sherrod Brown', 'Maria Cantwell', 'Ben Cardin', 'Tom Carper', 'Bob Casey Jr.', 'Chris Coons', 'Catherine Cortez Masto', 'Tammy Duckworth', 'Dick Durbin', 'Dianne Feinstein', 'Kristen Gillibrand', 'Kamala Harris', 'Maggie Hassan', 'Martin Heinrich', 'Mazie Hirono', 'Doug Jones', 'Tim Kaine', 'Amy Klobuchar', 'Patrick Leahy', 'Joe Manchin', 'Edward Markey', 'Robert Menendez', 'Jeff Merkley', 'Chris Murphy', 'Patty Murray', 'Gary Peters', 'Jack Reed', 'Jacky Rosen', 'Brian Schatz', 'Chuck Schumer', 'Jeanne Shaheen', 'Kyrsten Sinema', 'Tina Smith', 'Debbie Stabenow', 'Jon Tester', 'Tom Udall', 'Chris Van Hollen', 'Mark Warner', 'Elizabeth Warren', 'Sheldon Whitehouse', 'Ron Wyden', 'Angus King', 'Bernie Sanders', 'Susan Collins', 'Mitt Romney', 'Lamar Alexander', 'John Barrasso', 'Marsha Blackburn', 'Roy Blunt', 'John Boozman', 'Mike Braun', 'Richard Burr', 'Shelley Moore Capito', 'Bill Cassidy', 'John Cornyn', 'Tom Cotton', 'Kevin Cramer', 'Michael Crapo', 'Ted Cruz', 'Steve Daines', 'Michael Enzi', 'Joni Ernst', 'Deb Fischer', 'Cory Gardner', 'Lindsey Graham', 'Charles Grassley', 'Josh Hawley', 'John Hoeven', 'Cindy Hyde-Smith', 'James Inhofe', 'Ron Johnson', 'John Kennedy', 'James Lankford', 'Mike Lee', 'Kelly Loeffler', 'Mitch McConnel', 'Martha McSally', 'Jerry Moran', 'Lisa Murkowski', 'Rand Paul', 'David Perdue', 'Rob Portman', 'Jim Risch', 'Pat Roberts', 'Michael Rounds', 'Marco Rubio', 'Ben Sasse', 'Rick Scott', 'Tim Scott', 'Richard Shelby', 'Dan Sullivan', 'John Thune', 'Thom Tillis', 'Patrick Toomey', 'Roger Wicker', 'Todd Young']

def getWebpage(name):
    req = requests.get(urlStub + name)
    if req.status_code == 200:
        print('Retrieved page of {}'.format(name))
        return bs4(req.content, 'html.parser')
    else:
        name = name + '_(politician)'
        req = requests.get(urlStub + name)
        if req.status_code == 200:
            print('Retrieved page of {}'.format(name))
            return bs4(req.content, 'html.parser')
        else:
            print('Failed to retrieve on name {}'.format(name))
            return None

def Test():
    test0 = getWebpage('Michael_Bennet')
    img = test0.select_one('img[alt*="{}" i]'.format())

    imageURL = 'http:' + img['src']
    print(imageURL)
    Image.open(requests.get(imageURL, stream=True).raw)

class Senator:
    def __init__(self, name, img):
        self.name = name
        self.img = img

outSenators = []

def go():
    for i in senators:
        print('{}\n'.format(i))
        
        adjName = ''
        for j in i:
            if j != ' ':
                adjName = adjName + j
            else:
                adjName = adjName + '_'
        
        lastName = i.split(' ')[1]
        
        req = getWebpage(adjName)
        img = req.select_one('img[alt*="{}" i]'.format(lastName))
        if i == 'Ron Johnson':
            req = getWebpage('Ron_Johnson_(Wisconsin_politician)')
            img = req.select_one('img[alt*="{}" i]'.format(lastName))
        if i == 'Mike Lee':
            req = getWebpage('Mike_Lee_(American_politician)')
            img = req.select_one('img[alt*="{}" i]'.format(lastName))
        if i == 'Dan Sullivan':
            req = getWebpage('Dan_Sullivan_(U.S._senator)')
            img = req.select_one('img[alt*="{}" i]'.format(lastName))


        if img is None:
            img = req.select_one('img[alt*="{}" i]'.format('Official'))
            
        if img is None:
            req = getWebpage(adjName+'_(politician)')
            img = req.select_one('img[alt*="{}" i]'.format(lastName))
            
        if img is None:
            img = req.select_one('img[alt*="{}" i]'.format('Official'))
        

        imgU = 'http:' + img['src']
        outSenators.append(Senator(i, imgU))


go()

toJS = []
for i in outSenators:
    toJS.append(i.img)

print(toJS)
    
