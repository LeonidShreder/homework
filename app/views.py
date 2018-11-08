import app.models

@app.route('/ping', method=['GET'])
def ping():
    return  '{"status": "alive"}'
