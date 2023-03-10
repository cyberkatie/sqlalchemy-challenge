# sqlalchemy-challenge
Penn Bootcamp module 10 assignment

# Part 1. Analyze and Explore the Climate Data

* Used the SQLAlchemy create_engine() function to connect to the SQLite database.
* Used the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.
* Linked Python to the database by creating a SQLAlchemy session.
* Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections

*Precipitation Analysis
  * Found the most recent date in the dataset.
  * Used that date to get the previous 12 months of precipitation data by querying the previous 12 months of data.
  * Selected only the "date" and "prcp" values.
  * Loaded the query results into a Pandas DataFrame, and set the index to the "date" column.
  * Sorted the DataFrame values by "date".
  * Plotted the results
  * Used Pandas to print the summary statistics for the precipitation data

*Station Analysis
  * Designed a query to calculate the total number of stations in the dataset.
  * Designed a query to find the most-active stations (that is, the stations that have the most rows)
      * Listed the stations and observation counts in descending order.
  * Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query
  * Designed a query to get the previous 12 months of temperature observation (TOBS) data
      * Filtered by the station that has the greatest number of observations.
  * Queried the previous 12 months of TOBS data for that station.
  * Plotted the results as a histogram with bins=12

# Part 2. Design the Climate App

* Used Flask to create the routes

* (/) Start at the homepage.

List all the available routes.

* (/api/v1.0/precipitation) Converted the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Returned the JSON representation of your dictionary.

* (/api/v1.0/stations) Returned a JSON list of stations from the dataset.

* (/api/v1.0/tobs) Queryied the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

* (/api/v1.0/<start>) and (/api/v1.0/<start>/<end>)

Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
