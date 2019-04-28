from flask import Flask, request, render_template
import tinydb
import uuid
import json

app = Flask(__name__)

@app.before_first_request
def setup():
    env_db = tinydb.TinyDB('environments.json')
    env_db.insert({'name' : 'default', 'url' : 'http://localhost:8888'})
    
    notebook_db = tinydb.TinyDB('notebooks.json')
    blank_nb = {'cells' : [],
                'metadata' : {'display_name' : 'Python 3',
                              'language' : 'python',
                              'name' : 'python3'},
                'language_info' : {},
                'nbformat' : 4,
                'nbformat_minor' : 2}
    
    notebook_db.insert({'uuid' : uuid.UUID(int=1).hex,
                        'title' : 'Default DB notebook',
                        'description' : 'Default DB notebook entry',
                        'notebook' : blank_nb})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notebooks')
def list_notebooks():
    db = tinydb.TinyDB('notebooks.json')
    return render_template('notebooks.html', notebooks=db.all())        
    
@app.route('/notebooks/<uuid>')
def notebook(uuid):
    db = tinydb.TinyDB('notebooks.json')
    record = db.get(tinydb.where('uuid') == uuid)
    if not record:
        return {}
    else:
        return json.dumps(record)

@app.route('/stages', methods=['POST'])
def stages():
    db = tinydb.TinyDB('notebooks.json')
    js = request.get_json(force=True)
    for field in ['title', 'description', 'notebook']:
        if field not in js:
            msg = "invalid js on POST to /notebooks, missing %s" % field
            return msg, 404
    u = uuid.uuid4()
    js['uuid'] = u.hex
    db.insert(js)
    return u.hex

@app.route('/environments', methods=['GET', 'POST'])
def environments():
    db = tinydb.TinyDB('environments.json')
    if request.method == 'GET':
        return json.dumps(db.all())
    else:
        js = request.get_json(force=True)
        for field in ['name', 'url']:
            if field not in js:
                msg = "invalid js on POST to /environments, missing %s" % field
                return msg, 404
        q = (tinydb.where('name') == js['name']) & (tinydb.where('url') == js['url'])
        if not db.get(q):
            db.insert(js)
        return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

        