from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id,
                 tables,
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tables = tables
        self.expected_result=[0,0]

    def execute(self, context):
        redshift_hook = PostgresHook(self.redshift_conn_id)
        for table, exp_result in zip(self.tables, self.expected_result):
            records = redshift_hook.get_records(f"SELECT COUNT(*) FROM {table}")
            if len(records) == exp_result or len(records[0]) == exp_result:
                raise ValueError(f"Data quality check failed. {table} returned no results")
            num_records = records[0][0]
            if num_records == exp_result:
                raise ValueError(f"Data quality check failed. {table} contained 0 rows")
            self.log.info(f"Data quality on table {table} check passed with {records[0][0]} records")
