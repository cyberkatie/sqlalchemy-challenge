# 1. Import Flask
from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################

# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    
    """Return the most recent 12 months of precipitation"""
    # Query
    results = session.query(measurement.date, measurement.prcp)
    
    prcp_data = []
    result_dict = {}
    result_dict['date'] = date
    result_dict['prcp'] = prcp
    
    prcp_data.append(result_dict)
    session.close()

    return jsonify(prcp_data)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    stations = session.query(station.station).all()
    
    session.close()
    
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stations))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():

# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)