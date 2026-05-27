from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    if request.args.get('action') == 'login':
        print("[FAKE] Login intercepted")
        return Response(
            '{"message":"Auth Fail","status":"success"}',
            status=200,
            headers={
                'Content-Type': 'application/json',
                'Content-Length': '42',
                'Connection': 'keep-alive',
                'Server': 'PythonAnywhere'
            }
        )
    
    return Response('{}', status=200)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
