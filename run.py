# export FLASK_APP=market.py
# export FLASK_DEBUG=1
# flask run
from market import app

if __name__ == '__main__':
    app.run(debug=True)