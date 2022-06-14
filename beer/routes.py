import json

from flask import request, Response, render_template
from beer import app, db
from .keg import Keg
from .batch import Batch
from .vote import Vote

USER_ID = 'ZssoJ8xEdPSgJZ6anvFHY9fuXXr1'
API_KEY = 'J7WQ9sV0Vl7COiiB8z4pt27dPfGIrM9MOVmUqgxz223HOlTnFJTnhjEBySebV0B7'

@app.route('/')
def homepage():
    #loggin.debug('Homepage Called')
    #return Response('Homepage, Welcome!', mimetype='text/html', status=200)
    return render_template('home.html')

@app.route('/1')
def otherhome():
    return render_template('home.html')

@app.route('/sync')
def sync():
    #db.session.no_autoflush()
    _json = Batch.getBatches()
    db.session.commit()
    return Response(json.dumps(_json), mimetype='application/json', status=200)

@app.route('/list')
def list_beers():
    hello = 1
    #get database list of currently kegged batches
    #return render template

@app.route('/list/more_info/<int:_id>')
def more_info(_id):
    hello = 1
    #display additional info for selected batch
    #return render template

@app.route('/list/vote/<int:_id>', methods=['POST'])
def vote(_id):
    hello = 1
    #{'keg_index': 1, 'batch_id': 1, 'stars': 5, 'name': 'Bobby Douglass'}
    #process vote
    #return render template

"""
@app.route('/grav/<int:_id>/calibrate/<int:_index>', methods=['POST'])
def calibrate_grav(_id, _index):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        grav = db.session.query(Grav).filter_by(id=_id).first()
        grav.begin_calibration(index=_index)
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/grav/<int:_id>/update', methods=['POST'])
def update_grav(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        grav = db.session.query(Grav).filter_by(id=_id).first()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/grav/create', methods=['POST'])
def create_grav():
    print("/grav/create Called")
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        grav = Grav(int(_data['_id']), str(_data['name']), str(_data['grav_key']))
        db.session.add(grav)
        db.session.commit()
        print("/grav/create SUCCESS")
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/monitor', methods=['POST'])
def read_temp(_id):
    _data = request.json
    carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
    if _data['rpi_key'] == carboy.rpi_key:
        time.sleep(2)
        carboy.manageTemp(_data['loop_starting_time'], _data['readings0'], _data['readings1'], _data['loop_count'])
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("BAD RPI KEY", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/start_batch', methods=['POST'])
def start_batch(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
        carboy.current_batch = str(_data['batch_name'])
        carboy.target_temp = int(_data['target_temp'])
        carboy.is_brewing = True
        db.session.commit()

        try:
            grav = db.session.query(Grav).filter_by(id=int(_data['grav_id'])).first()
            grav.current_batch = str(_data['batch_name'])
            grav.is_brewing = True
            db.session.commit()
        except Exception as e:
            hello = 1

        print("TEMP LOCATION 1")
        carboy.startTempManagement()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)
    # _reqd = {
    #    "grav_id": 0,
    #    "carboy_id": 0,
    #    "batch_name": "HELLO",
    #    "target_temp": 85
    # }


@app.route('/carboy/<int:_id>/stop_batch', methods=['POST'])
def stop_batch(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
        carboy.is_brewing = False
        db.session.commit()

        carboy.stopTempManagement()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/update/ip', methods=['POST'])
def update_carboy(_id):
    _data = request.json
    # carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
        carboy.smartplug_ip = str(_data['_ip'])
        db.session.commit()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/create', methods=['POST'])
def create_carboy():
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = Carboy(int(_data['_id']), str(_data['name']), str(_data['carboy_key']))
        db.session.add(carboy)
        db.session.commit()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/delete', methods=['POST'])
def delete_carboy(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = db.session.query(Carboy).filter_by(id=_id).first()
        db.session.delete(carboy)
        db.session.commit()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/grav/<int:_id>/delete', methods=['POST'])
def delete_grav(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        grav = db.session.query(Grav).filter_by(id=_id).first()
        db.session.delete(grav)
        db.session.commit()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/grav/print', methods=['POST'])
def print_gravs():
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        all_gravs = db.session.query(Grav).all()
        results = "\n\nGRAVITY SENSORS IN DB...\n\n"
        for grav in all_gravs:
            results = "{}ID: {}, Name: {}, Unique: {}\n".format(results, grav.id, grav.name, grav.grav_key)

        print(results)
        return Response("{}".format(results), mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/print', methods=['POST'])
def print_carboys():
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        all_carboys = db.session.query(Carboy).all()
        results = "\n\nCARBOYS IN DB...\n\n"
        for carboy in all_carboys:
            results = "{}ID: {}, Name: {}, Unique: {}\n".format(results, carboy.id, carboy.name, carboy.rpi_key)

        print(results)
        return Response("{}".format(results), mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/on')
def plug_on(_id):
    carboy = db.session.query(Carboy).filter_by(id=_id).first()
    carboy.turn_plug_on()
    return Response("Turning smart plug on", mimetype="text/html", status=200)


@app.route('/carboy/<int:_id>/off')
def plug_off(_id):
    carboy = db.session.query(Carboy).filter_by(id=_id).first()
    carboy.turn_plug_off()
    return Response("Turning smart plug off", mimetype="text/html", status=200)ketio.emit('mqtt_message', data=data)

#    _data = request.json
#    _copy = _data
#    grav = db.session.query(Grav).filter_by(grav_key=str(_data['grav_key'])).first()
#    try:
#        grav.addPacket(_copy)
#        print("/ SUCCESS")
#        return Response("Gud jahb", mimetype="text/html", status=200)
#    except Exception as e:
#        return Response("Bad grav_key???", mimetype="text/html", status=401)

# reqd_json = {
#    "name": "",
#    "grav_key": "OJNRljnfgljnALJBlbOBhyvIBojnKHBJ",
#    "temp": float(75.5),
#    "acc_x": float(1.0),
#    "acc_y": float(-1.0),
#    "acc_z": float(0.0),
# }

@app.route('/grav/<int:_id>/calibrate/<int:_index>', methods=['POST'])
def calibrate_grav(_id, _index):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        grav = db.session.query(Grav).filter_by(id=_id).first()
        grav.begin_calibration(index=_index)
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/grav/<int:_id>/update', methods=['POST'])
def update_grav(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        grav = db.session.query(Grav).filter_by(id=_id).first()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/grav/create', methods=['POST'])
def create_grav():
    print("/grav/create Called")
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        grav = Grav(int(_data['_id']), str(_data['name']), str(_data['grav_key']))
        db.session.add(grav)
        db.session.commit()
        print("/grav/create SUCCESS")
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/monitor', methods=['POST'])
def read_temp(_id):
    _data = request.json
    carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
    if _data['rpi_key'] == carboy.rpi_key:
        time.sleep(2)
        carboy.manageTemp(_data['loop_starting_time'], _data['readings0'], _data['readings1'], _data['loop_count'])
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("BAD RPI KEY", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/start_batch', methods=['POST'])
def start_batch(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
        carboy.current_batch = str(_data['batch_name'])
        carboy.target_temp = int(_data['target_temp'])
        carboy.is_brewing = True
        db.session.commit()

        try:
            grav = db.session.query(Grav).filter_by(id=int(_data['grav_id'])).first()
            grav.current_batch = str(_data['batch_name'])
            grav.is_brewing = True
            db.session.commit()
        except Exception as e:
            hello = 1

        print("TEMP LOCATION 1")
        carboy.startTempManagement()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)
    # _reqd = {
    #    "grav_id": 0,
    #    "carboy_id": 0,
    #    "batch_name": "HELLO",
    #    "target_temp": 85
    # }


@app.route('/carboy/<int:_id>/stop_batch', methods=['POST'])
def stop_batch(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
        carboy.is_brewing = False
        db.session.commit()

        carboy.stopTempManagement()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/update/ip', methods=['POST'])
def update_carboy(_id):
    _data = request.json
    # carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = db.session.query(Carboy).filter_by(id=int(_id)).first()
        carboy.smartplug_ip = str(_data['_ip'])
        db.session.commit()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/create', methods=['POST'])
def create_carboy():
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = Carboy(int(_data['_id']), str(_data['name']), str(_data['carboy_key']))
        db.session.add(carboy)
        db.session.commit()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/delete', methods=['POST'])
def delete_carboy(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        carboy = db.session.query(Carboy).filter_by(id=_id).first()
        db.session.delete(carboy)
        db.session.commit()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/grav/<int:_id>/delete', methods=['POST'])
def delete_grav(_id):
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        grav = db.session.query(Grav).filter_by(id=_id).first()
        db.session.delete(grav)
        db.session.commit()
        return Response("Gud jahb", mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/grav/print', methods=['POST'])
def print_gravs():
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        all_gravs = db.session.query(Grav).all()
        results = "\n\nGRAVITY SENSORS IN DB...\n\n"
        for grav in all_gravs:
            results = "{}ID: {}, Name: {}, Unique: {}\n".format(results, grav.id, grav.name, grav.grav_key)

        print(results)
        return Response("{}".format(results), mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/print', methods=['POST'])
def print_carboys():
    _data = request.json
    if _data['app_key'] == "HGgHBlgKJHVkjydIOUoutwUOITghcHVB":
        all_carboys = db.session.query(Carboy).all()
        results = "\n\nCARBOYS IN DB...\n\n"
        for carboy in all_carboys:
            results = "{}ID: {}, Name: {}, Unique: {}\n".format(results, carboy.id, carboy.name, carboy.rpi_key)

        print(results)
        return Response("{}".format(results), mimetype="text/html", status=200)
    return Response("Unauthorized", mimetype="text/html", status=401)


@app.route('/carboy/<int:_id>/on')
def plug_on(_id):
    carboy = db.session.query(Carboy).filter_by(id=_id).first()
    carboy.turn_plug_on()
    return Response("Turning smart plug on", mimetype="text/html", status=200)


@app.route('/carboy/<int:_id>/off')
def plug_off(_id):
    carboy = db.session.query(Carboy).filter_by(id=_id).first()
    carboy.turn_plug_off()
    return Response("Turning smart plug off", mimetype="text/html", status=200)

"""
