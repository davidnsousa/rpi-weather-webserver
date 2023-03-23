import Adafruit_DHT
import RPi.GPIO as GPIO
from flask import Flask,render_template

sensor = Adafruit_DHT.DHT11
pin = 4

app = Flask(__name__)

@app.route('/')
def index():
    H, T = Adafruit_DHT.read_retry(sensor, pin)
    data={
        'H':H,
        'T':T,
    }
    return render_template('index.html', data=data)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')