from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

# Define the second DAG
dag_2 = DAG(
    'dag_2',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
)

# Define tasks in DAG 2
start = DummyOperator(
    task_id='start',
    dag=dag_2,
)

end = DummyOperator(
    task_id='end',
    dag=dag_2,
)

# Define the task sequence
start >> end
