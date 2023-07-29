# Applies all base migrations that haven't been applied and all chosen recipe
# migrations that haven't been applied yet.

import os
import sys
from scripts.connectDB import connectDB

BASE_DIRECTORY_PATH = "./migrations/base"
RECIPE_DIRECTORY_PATH = "./migrations/recipe/"

def applyBaseMigrations(db):
    sql = "SELECT COUNT(migrationName) FROM AppliedRecipeMigrations WHERE migrationName = 'BASE';"
    with db.cursor(buffered = True) as cursor:
        cursor.execute(sql)
        appliedBase = cursor.fetchall()[0][0]

    if not appliedBase:
        # Mark the base migrations as having been applied

        sql = "INSERT INTO AppliedRecipeMigrations (migrationNAme) VALUES ('BASE');"
        with db.cursor(buffered = True) as cursor:
            cursor.execute(sql)
        
        baseDirectory = os.fsencode(BASE_DIRECTORY_PATH)

        for filename in os.listdir(baseDirectory):
            filename = filename.decode("utf-8")
            if filename.endswith('.sql'):
                with open(os.path.join(BASE_DIRECTORY_PATH, filename), "r") as f:
                    with db.cursor(buffered = True) as cursor:
                        for l in f.readlines():
                            if l.strip():
                                cursor.execute(l)
                
    else:
        print("Base migrations have already been applied.")
    
    db.commit()

def applyRecipeMigrations(db, recipeMigrations):
    cursor = db.cursor(buffered = True)

    for keyword in recipeMigrations:
        sql = f"SELECT COUNT(migrationName) FROM AppliedRecipeMigrations WHERE migrationName = 'RECIPE-{keyword}';"
        cursor.execute(sql)
        appliedMigration = cursor.fetchall()[0][0]

        if not appliedMigration:
            with open(f"{RECIPE_DIRECTORY_PATH}{keyword}.sql", "r") as f:
                for l in f.readlines():
                    if l.strip():
                        cursor.execute(l)
            db.commit()
        else:
            print(f"{keyword} migration has already been applied.")


if __name__ == '__main__':
    recipeMigrations = sys.argv[1:]

    db = connectDB()

    # Always apply base migrations
    applyBaseMigrations(db)

    # If any, apply recipe migrations that have been given as command line
    # arguments
    recipeMigrations = sys.argv[1:]
    if recipeMigrations:
        applyRecipeMigrations(db, recipeMigrations)
    