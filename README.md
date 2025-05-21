# flood-data

Project to demonstrate cloud ETL/ELT on different platforms using UK Rainfall & Flood data.

Project contains:
- EDA and API query notebooks
- Historic data extract notebooks
- Pipelines for ETL
- Visualisation
- Modelling - simple flood prediction ML

This uses Environment Agency rainfall, flood and river level data from the real-time data API (Beta)

## Data sources & documentation

Rainfall:
https://environment.data.gov.uk/flood-monitoring/doc/rainfall

Flood-monitoring:
https://environment.data.gov.uk/flood-monitoring/doc/reference

API Demo:
https://github.com/epimorphics/rainfall-api-demonstrator

## Pipelines

- AWS
  - AWS lambda to query API and return latest readings (15 mins)
  - Filter for specified subset of stations (possibly by radius from location or catchment)
  - Append to parquet file in S3
 
##Visualisation
