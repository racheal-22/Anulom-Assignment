from flask import Flask, request, render_template
from flasgger import Swagger
from models import db, RequestRecord
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sum_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Swagger(app)
db.init_app(app)

# Create DB tables immediately at startup
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compute', methods=['GET', 'POST'])
def compute():
    if request.method == 'POST':
        numbers_input = request.form.get('numbers')
        try:
            numbers = [int(n.strip()) for n in numbers_input.split(',') if n.strip()]
            numbers_str = json.dumps(sorted(numbers))
            existing = RequestRecord.query.filter_by(numbers=numbers_str).first()

            if existing:
                return render_template('compute.html', result=existing.result, cached=True,
                                       txn_id=existing.id, timestamp=existing.timestamp)
            else:
                result = sum(numbers)
                new_record = RequestRecord(numbers=numbers_str, result=result)
                db.session.add(new_record)
                db.session.commit()
                return render_template('compute.html', result=result, cached=False,
                                       txn_id=new_record.id, timestamp=new_record.timestamp)
        except:
            return render_template('compute.html', error="Invalid input. Use comma-separated numbers.")

    return render_template('compute.html')

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    if request.method == 'POST':
        txn_id = request.form.get('txn_id')
        record = RequestRecord.query.filter_by(id=txn_id).first()
        if record:
            return render_template('transaction.html',
                                   numbers=json.loads(record.numbers),
                                   result=record.result,
                                   timestamp=record.timestamp)
        else:
            return render_template('transaction.html', error="Transaction ID not found.")
    return render_template('transaction.html')

@app.route('/about')
def about():
    return "<h2>Smart Sum Calculator - Built with Flask + SQLite</h2>"

if __name__ == '__main__':
    app.run(debug=True)
