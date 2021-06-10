# BGP API Scanner

This is the source code of BGP API Scanner of Hurricane Electric (HE), the code is written mostly in Python3.+.

The project support running on Linux, Windows and Mac OS X.

## Setup

To configure the db, we used docker:

```
docker run --name postgres-scan -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=db_scan -p 5433:5432 -d postgres
```

If you want to see or interactive with psql command line:

```
docker exec -tiu postgres postgres-scan psql
```

Install dependencies in virutal env:

```bash
> python3 -m venv env
> source env/bin/activate
(env)> pip install -r requirements.txt
```

## Usage

To run project:

```bash
(env)> flask run -h 0.0.0.0
```
