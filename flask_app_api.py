from flask import Flask, make_response
from prometheus_client import Counter, generate_latest
from prometheus_client.exposition import MetricsHandler

app = Flask(__name__)

# Create a Prometheus counter metric to count API calls
api_calls_total = Counter('api_calls_total', 'Total number of API calls')

@app.route('/')
def countapicalls():
    # incremental counter of api view
    api_calls_total.inc()
    #Add output to the page 
    response = make_response("<h1>Successful API Call</h1>", 200)
    return response


@app.route('/metrics')
def metrics():
    return generate_latest()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
