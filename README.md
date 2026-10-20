# Personal Financial Analysis System.

A Data Science and Machine Learning system for personal financial analysis, providing dashboards, data visualizations, financial indicators, forecasting, and reports for a comprehensive view of an individual's financial situation.

## Status.

Under development.

## Technologies:

- SQL.
- PostgreSQL.
- Python.
    - Matplotlib.
    - NumPy.
    - Pandas.
    - Scikit-learn.
    - SQLAlchemy.
    - Flask.
- Docker.
- Front-end.
    - HTML.
    - CSS.
    - JavaScript.

## How to run.

### Prerequisites.

- [Docker](https://www.docker.com/) with Docker Compose.

### Development.

1. Clone the repository:

    ```bash
    git clone https://github.com/devgustavosmota/personal_financial_analysis.git
    cd personal_financial_analysis
    ```

2. Create your environment file and fill in the values:

    ```bash
    cp .env.example .env
    ```

    Required variables: `SECRET_KEY`, `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`. The app will not start if any is missing.

3. Build and start:

    ```bash
    docker compose up --build
    ```

    The app is available at http://localhost:5000, and the database at `127.0.0.1:5433` for local tools.

    To stop (data is kept in a Docker volume):

    ```bash
    docker compose down
    ```

    To also delete the database data: `docker compose down -v`.

### Tests

Uses throwaway credentials and a separate project name so it never touches your dev database:

```bash
docker compose -p pfa_test -f compose.yaml -f compose.test.yaml run --rm web
docker compose -p pfa_test -f compose.yaml -f compose.test.yaml down -v
```
