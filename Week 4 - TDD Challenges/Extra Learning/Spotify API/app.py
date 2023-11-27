from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['GET'])
def callback():
    # Retrieve the authorization code from the query parameters
    code = request.args.get('code')

    # Your code to handle the authorization code and exchange it for an access token
    # ...

    return f'Authorization code received: {code}'

if __name__ == '__main__':
    app.run(port=8888)