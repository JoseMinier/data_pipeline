FROM quay.io/astronomer/astro-runtime:12.5.0

RUN python -m venv dbt-env && \
    . dbt-env/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && \
    deactivate

