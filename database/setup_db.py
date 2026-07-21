import psycopg2
from pathlib import Path
from config import AIVEN_DATABASE_URL


def setup_db():
    base_dir= Path(__file__).resolve().parent.parent
    schema_path = base_dir / "database" / "schema.sql"
    seed_path = base_dir / "database" /"seed_data.sql"

    try:
       conn = psycopg2.connect(AIVEN_DATABASE_URL)
       cursor = conn.cursor()

       schema_text = schema_path.read_text(encoding='utf-8')
       cursor.execute(schema_text)

       seed_text = seed_path.read_text(encoding='utf-8')
       cursor.execute(seed_text)

       conn.commit()
       cursor.close()
       conn.close()

    except Exception as e:
        print(f"Error is {e}")    

if __name__ == "__main__":
    setup_db()        