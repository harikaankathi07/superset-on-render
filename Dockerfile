FROM apache/superset:latest

USER root

# Install extra dependencies
RUN pip install --no-cache-dir \
    Pillow \
    flask_cors \
    databricks-sql-connector \
    sqlalchemy-databricks \
    psycopg2-binary>=2.9

USER superset

# Set environment to production
ENV SUPERSET_ENV=production

# Copy Superset config
COPY superset_config.py /app/pythonpath/

# Optional: for local use, do not use .env in Railway
# COPY .env /app/

# Set Superset config path
ENV SUPERSET_CONFIG_PATH=/app/pythonpath/superset_config.py

# Expose default Superset port
EXPOSE 8088

# Initialize and run Superset
CMD ["bash", "-c", "\
  superset db upgrade && \
  superset fab create-admin \
    --username ${SUPERSET_USERNAME} \
    --firstname Admin \
    --lastname User \
    --email ${SUPERSET_EMAIL} \
    --password ${SUPERSET_PASSWORD} || true && \
  superset init && \
  gunicorn -w 2 -k gthread --timeout 120 -b 0.0.0.0:8088 'superset.app:create_app()'"]


