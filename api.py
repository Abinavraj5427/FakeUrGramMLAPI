from flask import Flask, jsonify, abort, send_from_directory, make_response
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Input, Dense, LeakyReLU, Dropout, \
  BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD, Adam
from PIL import Image
import random

app = Flask(__name__)


@app.route("/landscape/")
def landscape():
    noise = np.random.randn(1, 100)
    generator = tf.keras.models.load_model('landscapegen.h5', custom_objects={'LeakyReLU': tf.keras.layers.LeakyReLU})
    output = generator.predict(noise)
    output = (0.5 * output + 0.5)
    output = output.reshape(200,200,3)
    #print(output.shape)
    im = Image.fromarray((output * 255).astype(np.uint8))
    im.show()
    filename = '%030x' % random.randrange(16**30)
    im.save("./images/"+str(filename)+".png")
    # return jsonify({"about": "Hello World"})

    try:
        response = make_response(send_from_directory('./images', filename = filename+'.png', as_attachment = False))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-type'] = 'image/png'
        return response
    except FileNotFoundError:
        abort(404)

@app.route("/flower/")
def flower():
    noise = np.random.randn(1, 100)
    generator = tf.keras.models.load_model('cflowergen.h5', custom_objects={'LeakyReLU': tf.keras.layers.LeakyReLU})
    output = generator.predict(noise)
    output = (0.5 * output + 0.5)
    output = output.reshape(200,200,3)
    #print(output.shape)
    im = Image.fromarray((output * 255).astype(np.uint8))
    im.show()
    filename = '%030x' % random.randrange(16**30)
    im.save("./images/"+str(filename)+".png")
    # return jsonify({"about": "Hello World"})

    try:
        return send_from_directory(
            './images', filename = filename+'.png', as_attachment = False
        )
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)