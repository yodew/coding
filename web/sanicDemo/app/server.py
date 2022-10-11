
from app import my_app

if __name__ == "__main__":
    my_app.run(port=8181, host="127.0.0.1", debug=True, workers=1, access_log=True)
