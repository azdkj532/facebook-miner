import facebook
access_token = input( "Please input an usable token:\n")
APISyntax    = input( "Please input your APISyntax:\n")
fb = facebook.GraphAPI( access_token )

def recursive( source, syntax ):
    url = syntax
    while True:
        articles = source.get_object( url )
        for article in articles['data']:
            yield article
        try:
            url = articles['paging']['next'][32:]
        except KeyError:
            raise StopIteration

record = open( "record.txt", "w")
for article in get_articles( fb, APISyntax ):
    record.write( str(article) )
    record.write("\n")
record.close()
