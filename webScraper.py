import requests
from lxml import etree

urlStub = 'https://en.wikipedia.org/wiki/'
senators = ['Tammy Baldwin', 'Michael Bennet', 'Richard Blumethal', 'Cory Booker', 'Sherrod Brown', 'Maria Cantwell', 'Benjamin Cardin', 'Thomas Carper', 'Bob Casey', 'Chris Coons', 'Catherine Cortez Masto', 'Tammy Duckworth', 'Richard Durbin', 'Dianne Feinstein', 'Kristen Gillibrand', 'Kamala Harris', 'Maggie Hassan', 'Martin Heinrich', 'Mazie Hirono', 'Doug Jones', 'Tim Kaine', 'Amy Klobuchar', 'Patrick Leahy', 'Joe Manchin', 'Edward Markey', 'Robert Menendez', 'Jeff Merkley', 'Christopher Murphy', 'Patty Murray', 'Gary Peters', 'Jack Reed', 'Jacky Rosen', 'Brian Schatz', 'Chuck Schumer', 'Jeanne Shaheen', 'Kyrsten Sinema', 'Tina Smith', 'Debbie Stablenow', 'John Tester', 'Tom Udall', 'Chris Van Hollen', 'Mark Warner', 'Elizabeth Warren', 'Sheldon Whitehouse', 'Ron Wyden', 'Angus King', 'Bernie Sanders', 'Susan Collins', 'Mitt Romney', 'Lamar Alexander', 'John Barrasso', 'Marsha Blackburn', 'Roy Blunt', 'John Boozman', 'Mike Braun', 'Richard Burr', 'Shelley Moore Capito', 'Bill Cassidy', 'John Cornyn', 'Tom Cotton', 'Kevin Cramer', 'Michael Crapo', 'Ted Cruz', 'Steve Daines', 'Michael Enzi', 'Joni Ernst', 'Deb Fischer', 'Cory Gardner', 'Lindsey Graham', 'Charles Grassley', 'Josh Hawley', 'John Hoeven', 'Cindy Hyde-Smith', 'James Inhofe', 'Ron Johnson', 'John Kennedy', 'James Lankford', 'Mike Lee', 'Kelly Loeffler', 'Mitch McConnel', 'Martha McSally', 'Jerry Moran', 'Lisa Murkowski', 'Rand Paul', 'David Perdue', 'Rob Portman', 'Jim Risch', 'Pat Roberts', 'Michael Rounds', 'Marco Rubio', 'Ben Sasse', 'Rick Scott', 'Tim Scott', 'Richard Shelby', 'Dan Sullivan', 'John Thune', 'Thom Tillis', 'Patrick Toomey', 'Roger Wicker', 'Todd Young']

for i in senators:
    print(i)
    url = urlStub
