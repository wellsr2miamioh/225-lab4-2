import sqlite3

# Database file path, ensure this matches the path used in your Flask application
DATABASE = '/nfs/demo.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE)

def clear_contacts():
    """Clear all entries in the contacts table."""
    db = connect_db()
    db.execute('DELETE FROM contacts')
    db.commit()
    print('All contacts have been deleted from the database.')
    db.close()

if __name__ == '__main__':
    clear_contacts()
