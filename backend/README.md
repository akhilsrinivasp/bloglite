## Directory Structure

```
bloglite/
├── api
│   ├── __init__.py
│   ├── auth.py
│   ├── blog.py
│   ├── follow.py
│   ├── image.py
│   └── user.py
├── static
│   ├── image_data
│   ├── styles
│   └── background.jpg
├── templates
│   └── index.html
├── __init__.py
├── config.py
├── models.py
app.py
requirements.txt
```

## Config 
The Config File contains two Configs which can be swapped and used for development and production.

```python 
def create_app(config_class=LocalDevelopmentConfig):
    or
def create_app(config_class=ProductionConfig):
```

The `create_app` function is the main function which creates the app and registers the blueprints.

```python
def create_app(config_class=LocalDevelopmentConfig):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    ma.init_app(app)
    
    api = Api(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    JWTManager(app)
    
    api = register_api(api)
    
    with app.app_context():
        db.create_all() 
    return app, api
```

## Models
The `models.py` file contains the database models and the database initialization.

```python
User 
├── name
├── username
├── email
├── password
├── image
├── created_at
└── updated_at
 
Blog
├── title
├── content
├── image
├── author
├── created_at
└── updated_at

Follow 
├── follower
├── following
├── created_at
└── updated_at
```

## Setting up the Environment 

### .env file 
The `.env` file contains the environment variables which are used by the app. The `.env` file is not included in the repository.
The following environment variables are required for the app to run.
```bash
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_RUN_PORT=5050
FLASK_RUN_HOST=0.0.0.0
```

### Virtual Environment
The virtual environment is used to isolate the dependencies of the app from the system dependencies. The virtual environment is not included in the repository.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running the app
```bash
source venv/bin/activate
mkdir -p static/image_data

flask run 
```

## API Endpoints
The API endpoints are defined in the `api` directory. The endpoints are available in the api directory and they have been created using Flask-Restful.
The Endpoints are defined in the [YAML FILE](https://github.com/akhilsrinivasp/bloglite/blob/main/blite.yaml).