import facebook
access_token = input( "Please input an usable token:\n")
APISyntax    = input( "Please input your APISyntax:\n")
fb = facebook.GraphAPI( access_token )

def recursive( source, syntax ):
    articles = source.get_object( syntax )
    for article in articles['data']:
        yield article
    try:
        next_page = articles['paging']['next']
    except KeyError:
        raise StopIteration
    else:
        yield from recursive( source, next_page[32:] )

record = open( "record.txt", "w")
for article in recursive( fb, APISyntax ):
    record.write( str(article) )
    record.write("\n")
record.close()
