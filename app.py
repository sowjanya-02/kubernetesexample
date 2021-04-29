from flask import Flask
#from resources.routes import initialize_routes
import socket
app = Flask(__name__)
@app.route('/')
def home():
   hostname = socket.gethostname(
   return 'welcome to conn! store microservice is running on {} pod :)'.format(hostname)

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=8000)
