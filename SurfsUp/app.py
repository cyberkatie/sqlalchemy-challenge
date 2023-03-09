#Import Flask and sqlalchemy
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import pandas as pd
import datetime as dt

#Create an app
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

metadata = sqlalchemy.MetaData()
metadata.reflect(engine)
Base = automap_base(metadata=metadata)
Base.prepare()

# Save references to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################


#Define static routes
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
    #Calculate 12 months ago\
    year_ago = dt.date(2017, 8,23) - dt.timedelta(days = 365)
    
    # Query
    results = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= year_ago).all()
    
    session.close()

    return jsonify(results)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    stations_result = session.query(station.station).all()
    
    session.close()
    
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stations_result))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    tobs_result = session.query(measurement.station, measurement.tobs).\
    filter(measurement.station == 'USC00519281').all()
    
    session.close()
    
    return jsonify(tobs_result)

@app.route("/api/v1.0/<start>/<end>")
def start():
    session = Session(engine)
    
    year_ago = dt.date(2017, 8,23) - dt.timedelta(days = 365)
    start_result = session.query(measurement.tobs).\
    filter(measurement.date > year_ago).all()
    
    end_result = session.query(measurement.tobs).\
    filter(measurement.date >= year_ago).all()
    
    start_temps = {'min temp' : min(start_result), 'max temp' : max(start_result), 'avg temp' : np.mean(start_result)}
    end_temps = {'min temp' : min(end_result), 'max temp' : max(end_result), 'avg temp' : np.mean(end_result)}
    
    return jsonify(start_temps, end_temps)
    
#Define main behavior
if __name__ == "__main__":
    app.run(debug=True)