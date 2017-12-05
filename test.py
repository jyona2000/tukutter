def application(environ, start_response):




    status = '200 OK'

    header =  [('Content-Type', 'text/html')]

    html = 'hello python world'

    start_response(status,header)



    return [html.encode('utf-8')]
