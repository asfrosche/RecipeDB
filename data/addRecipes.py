import json
import sys
import traceback
from scripts.extractAPI import searchRecipes
from scripts.createMigration import createMigrationFromJSON

if __name__ == '__main__':
    try:
        args = sys.argv
        if len(args) < 3:
            raise ValueError
        count = int(args[1])
        keywords = args[2:]
        for keyword in keywords:
            with open(f"json/{keyword}.json", "w") as f:
                json.dump(searchRecipes(keyword, count), f)
            
            createMigrationFromJSON(f"{keyword}.json", keyword)
    except ValueError:
        traceback.print_exc()
        print("Usage: python addRecipes.py recipeCountPerKeyword recipeKeyword1 [recipeKeyword2 ...]")
