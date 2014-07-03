from OpenSSL import SSL

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('yourserver.key')
context.use_certificate_file('yourserver.crt')

app.run(host='127.0.0.1',port='12344', 
        debug = False/True, ssl_context=context)