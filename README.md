## Turbine Health UI

A Flask frontend application for quickly reviewing the health of turbines based off data obtained from an API call.

### How To Run

This Flask relies on the package manager [poetry](https://python-poetry.org/). This can be quickly installed via pip although this isn't advised due to potential dependency conflicts.

Once `poetry` is installed locally run the following in the repo root:

`poetry install` - to install its dependencies.
`poetry run python src/app.py` - to run the server in the virtual envrionment.

Once running the app will be available at `http://localhost:5000/`

### TODOs

- Testing - starting with unit testing `src/data_request.py`.
- pre-commits - setup linting/testing prior to pushing to a repo.
- Dockerfile - get this app containerised.
- CI/CD - get it deployed and on a URL and automate linting/testing.
- Further dashboards and data breakdowns e.g. piechart of WARNING/CRITICAL alarms.
- Table sorting to allow the end user to view the data how they'd like.