from beer import app, db

if __name__ == '__main__':
    try:
        db.create_all(app=app)
        app.run(debug=True, host='0.0.0.0', use_reloader=False)
    except (IndexError, ValueError) as e:
        print("usage: ./app.py port:int")
