from .flask_server import app as flask_app

flask_app.run(host='0.0.0.0', port=8080, load_dotenv=True, debug=True)
