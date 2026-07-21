import psycopg2
from config import AIVEN_DATABASE_URL
from src.custom_state import CustomState

def executor_node(state: CustomState) -> CustomState:
    try:
        conn = psycopg2.connect(AIVEN_DATABASE_URL)
        cursor = conn.cursor()

        sql_query = state['query'].strip()
        cursor.execute(sql_query)

        if sql_query.upper().startswith('SELECT'):
            result = cursor.fetchall()
        else:
            conn.commit()
            result = 'Done'

        cursor.close()
        conn.close()

        state['result'] = result

    except Exception as e:
        print(f'Error in executing is: {e}')
        state['result'] = []

    return state