# backend/run.py
from fracture_api import create_app

app = create_app()

if __name__ == '__main__':
    # Runs development server
    app.run(debug=True)