from app import create_app
import ssl

app = create_app()

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('certificate.pem', 'private_key.pem')
   
    app.run(host='northramp.ai', port=5000, ssl_context=context, debug=True)