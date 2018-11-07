import app.models
"""
@app.route('/ping', method=['GET'])
def category(categories_path):
    category = list(filter(lambda p: p['id'] == categorires_path, categorires))
    return category[0] if product else False 
    я это просто оставлю потом думаю будет нужно 
"""
@app.route('/ping', method=['GET'])
def ping():
    return  '{"status": "alive"}'
