import serial
app = Flask(__name__)
CORS(app)

connection = None  # Global variable to keep track of the serial connection

def create_connection(port='COM8', baud_rate=9600):
    global connection
    try:
        connection = serial.Serial(port, baud_rate)
        print(f"Successfully connected to {port} at {baud_rate} baud.")
        return connection, True
    except Exception as e:
        print(f"Failed to connect to {port} at {baud_rate} baud. Exception: {e}")
        return None, False

@app.route('/connect', methods=['POST'])
def connect():
    connection, success = create_connection()
    if success:
        return jsonify({'success': True, 'message': 'Connected successfully', 'comPort': 'COM8'})
    else:
        return jsonify({'success': False, 'message': 'Failed to connect'})

@app.route('/check_connection', methods=['GET'])
def check_connection():
    global connection
    if connection and connection.isOpen():
        return jsonify({'connected': True})
    else:
        return jsonify({'connected': False})


@app.route('/send_command', methods=['POST'])
def send_command():
    global connection
    command = request.json.get('command')
    try:
        if connection and connection.isOpen():
            x, y = command.split(',')
            connection.write(f"{x},{y}\n".encode())
            return jsonify({'success': True, 'message': 'Command sent successfully'})
        else:
            return jsonify({'success': False, 'message': 'Not connected to the device'})
    except Exception as e:
        print(f"Exception in sending command: {e}")
        return jsonify({'success': False, 'message': 'An error occurred while sending the command'})

@app.route('/disconnect', methods=['POST'])
def disconnect():
    global connection
    try:
        if connection and connection.isOpen():
            connection.close()
            print("Successfully disconnected")
            return jsonify({'success': True, 'message': 'Disconnected successfully'})
        else:
            return jsonify({'success': False, 'message': 'Already disconnected or never connected'})
    except Exception as e:
        print(f"Exception in disconnecting: {e}")
        return jsonify({'success': False, 'message': 'An error occurred while disconnecting'})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)