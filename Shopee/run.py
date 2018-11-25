from webapp import create_app
from webapp import create_db


# App initialization
app = create_app()
database = create_db()


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
