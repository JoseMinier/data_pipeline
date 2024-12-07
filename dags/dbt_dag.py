import os
from datetime import datetime
from cosmos import DbtDag, ProfileConfig, ProjectConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

# Configuración del perfil de conexión
profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "dbt_db", "schema": "dbt_schema"},
    )
)

# Definición del DAG
dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/data_pipeline"),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path="C:/Users/user/dbt-env/Scripts/dbt.exe",  # Aquí se agrega la ruta correcta
    ),
    schedule_interval="@daily",
    start_date=datetime(2024, 12, 7),
    catchup=False,
    dag_id="dbt_dag"
)
