def process_http_request(environ, start_response):
    status = '200 OK'
    qs = environ.get('QUERY_STRING','')
    data = qs.replace('&','\n').encode()
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
    ]
    start_response(status, response_headers)
    text = 'Here be dragons'.encode('utf-8')
    return iter([data])