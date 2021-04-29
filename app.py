from flask import Flask
#from resources.routes import initialize_routes
import socket
app = Flask(__name__)
#app = create_app()
#@app.route('/')
#def hello():
   #hostname = socket.gethostname()
   #return 'welcome to conn! store microservice is running on {} pod :)'.format(hostname)
@app.route('/')
def home():
   hostname = socket.gethostname()
   #local_ip = socket. gethostbyname(localhost)
   return 'welcome to conn! store microservice is running on {} pod :)'.format(hostname)

if __name__ == "__main__":
      #connservices = "0.0.0.0"
      app.run(host="0.0.0.0", port=9876)