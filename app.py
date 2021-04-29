from flask import Flask
#from resources.routes import initialize_routes
import socket
app = Flask(__name__)
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
@app.route('/')
def home():
   hostname = socket.gethostname(
   return 'welcome to conn! store microservice is running on {} pod :)'.format(hostname)

if __name__ == "__main__":
<<<<<<< Updated upstream
      app.run(host="0.0.0.0", port=9876)
=======
      app.run(host="0.0.0.0", port=9876)
>>>>>>> Stashed changes
