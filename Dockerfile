FROM apache/airflow:2.0.1-python3.9

USER root
RUN apt-get update && \
    ldconfig

USER airflow
WORKDIR ${AIRFLOW_HOME}
EXPOSE 8080
