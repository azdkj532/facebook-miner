import facebook
access_token = input( "Please input an usable token:\n")
fb = facebook.GraphAPI( access_token )

def recursive( source, syntax ):
    articles = source.get_object( syntax )
    for article in articles['data']:
        yield article
    try:
        next_page = articles['paging']['next']
    except KeyError:
        print("test")
        raise StopIteration
    else:
        yield from recursive( source, next_page[32:] )

record = open( "record.txt", "w")
for article in recursive( fb, "314357341996385/feed?fields=id,message" ):
    record.write( str(article) )
    record.write("\n")
record.close()
