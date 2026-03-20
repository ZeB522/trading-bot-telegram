from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        logging.info(f'Received webhook data: {data}')
        # Process the data here
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        logging.error(f'Error processing webhook: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/resultado', methods=['GET'])
def resultado():
    try:
        # Example results data
        results = {'message': 'Success'}
        return jsonify(results), 200
    except Exception as e:
        logging.error(f'Error fetching results: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)