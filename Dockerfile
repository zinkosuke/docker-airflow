##################################################
# Local development environment.
##################################################
FROM python:3.8-slim as development

ENV PYTHONDONTWRITEBYTECODE=1
ENV AIRFLOW_HOME=/opt/config
ENV AIRFLOW_APP_DIR=/opt/airflow
ENV AIRFLOW_LOG_DIR=/var/log/airflow
ENV AIRFLOW_DB_URL=sqlite:////tmp/sqlite.airflow.db

WORKDIR ${AIRFLOW_APP_DIR}

COPY poetry.lock .
COPY pyproject.toml .

RUN set -x \
 && mkdir -p ${AIRFLOW_HOME} \
 && mkdir -p ${AIRFLOW_LOG_DIR} \
 && apt-get update -yqq \
 && apt-get upgrade -yqq \
 && pip install -U pip setuptools poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root \
 && apt-get autoremove -yqq --purge \
 && apt-get -y clean \
 && rm -rf \
        /tmp/* \
        /usr/share/doc \
        /usr/share/doc-base \
        /usr/share/man \
        /var/lib/apt/lists/* \
        /var/tmp/* \
        poetry.lock \
        pyproject.toml

##################################################
# Production environment.
##################################################
FROM python:3.8-slim as production

ARG OWNER=airflow

ENV AIRFLOW_HOME=/opt/config
ENV AIRFLOW_APP_DIR=/opt/airflow
ENV AIRFLOW_LOG_DIR=/var/log/airflow
ENV AIRFLOW_DB_URL=sqlite:////tmp/sqlite.airflow.db

COPY --from=development /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=development /usr/local/bin/airflow /usr/local/bin/airflow
COPY --from=development /usr/local/bin/celery /usr/local/bin/celery
COPY --from=development /usr/local/bin/gunicorn /usr/local/bin/gunicorn

WORKDIR ${AIRFLOW_APP_DIR}

COPY config/ ${AIRFLOW_HOME}/
COPY airflow/ .

RUN set -x \
 && useradd -r -s /bin/false ${OWNER} \
 && mkdir -p ${AIRFLOW_LOG_DIR} \
 && chown -R ${OWNER} ${AIRFLOW_LOG_DIR} \
 && chown -R ${OWNER} ${AIRFLOW_HOME} \
 && apt-get update -yqq \
 && apt-get upgrade -yqq \
 && apt-get autoremove -yqq --purge \
 && apt-get -y clean \
 && rm -rf \
        /tmp/* \
        /usr/share/doc \
        /usr/share/doc-base \
        /usr/share/man \
        /var/lib/apt/lists/* \
        /var/tmp/*

USER ${OWNER}
EXPOSE 8080
