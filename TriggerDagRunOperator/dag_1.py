from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.utils.dates import days_ago

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

# Define the first DAG
dag_1 = DAG(
    'dag_1',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
)

# Define tasks in DAG 1
start = DummyOperator(
    task_id='start',
    dag=dag_1,
)

# Trigger DAG 2
trigger_dag_2 = TriggerDagRunOperator(
    task_id='trigger_dag_2',
    trigger_dag_id='dag_2',  # The DAG ID of the DAG to trigger
    dag=dag_1,
)

# Define the task sequence
start >> trigger_dag_2
