from datetime import timedelta


def default_args(**kwargs):
    return {
        "owner": "airflow",
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "depends_on_past": False,
        "pool": "default_pool",
        "retries": 1,
        "retry_delay": timedelta(minutes=5.0),
        **kwargs,
    }
