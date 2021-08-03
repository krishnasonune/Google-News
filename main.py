from GoogleNews import GoogleNews     # pip install Google news and import it


# define language and region according to your preference
Gnews = GoogleNews(lang='en', region='india')

Gnews = GoogleNews(period='7d')   # define period in days

Gnews = GoogleNews(start='27/07/2021',end='03/08/2021')
# set custom range of date to get highlights of that day

Gnews.search('Infosys')
# provide the topic in search function to get more related news



result = Gnews.result()
# getting result from here and passing it in the list

for x in result:
    print("-"*50)
    print("title--", x['title'])
    print("Date/Time--", x['date'])
    print("Description--", x['desc'])
    print("Link--", x['link'])
    print("Image--", x['img']) # image might not load but you'll get image.gif link directly from google
