import sqlite3
import os

def run_sql_file(db_path, sql_file):
    """Run SQL file on database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    
    try:
        cursor.executescript(sql_script)
        print(f"✓ {os.path.basename(sql_file)}")
    except Exception as e:
        print(f"✗ {os.path.basename(sql_file)}: {e}")
    
    conn.commit()
    conn.close()

def main():
    db_path = 'database/energy_db.sqlite'
    
    # Ensure database directory exists
    os.makedirs('database', exist_ok=True)
    
    # Run migrations
    migrations = [
        'database/migrations/001_create_energy_data.sql',
        'database/migrations/002_create_forecasts.sql',
        'database/migrations/003_create_grid_optimizations.sql',
        'database/migrations/004_create_carbon_emissions.sql',
        'database/seeds/sample_data.sql'
    ]
    
    print("🔧 Setting up database...")
    for migration in migrations:
        if os.path.exists(migration):
            run_sql_file(db_path, migration)
        else:
            print(f"⚠ File not found: {migration}")
    
    print("\n✅ Database setup complete!")

if __name__ == "__main__":
    main()