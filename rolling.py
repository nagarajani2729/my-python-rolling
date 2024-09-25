# rolling.py
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roll-dice', methods=['GET'])
def roll_dice():
    dice_result = random.randint(1, 6)
    return jsonify({'result': dice_result})

if __name__ == '__main__':
    app.run(debug=True)
