import facebook

access_token = input( "Please input an usable token:\n")
APISyntax    = input( "Please input your APISyntax:\n")
fb = facebook.GraphAPI( access_token )

def get_articles( source, syntax ):
    articles = source.get_object( syntax )
    for article in articles['data']:
        yield article
    try:
        next_page = articles['paging']['next']
    except KeyError:
        raise StopIteration
    else:
        yield from get_articles( source, next_page[32:] )


record = open( "record.txt", "w")
for article in get_articles( fb, APISyntax ):
    record.write( str(article) )
    record.write("\n")
record.close()
