import requests

# Max size of a BLOB type in MySQL
MAX_IMAGE_SIZE = 65535

def getAPIrecipes(keyword, count):
    app_id = '73cf0996'
    app_key = '4b789708cddb597453e31879162878ae'
    result = requests.get(f'https://api.edamam.com/search?q={keyword}&imageSize=SMALL&to={count}&app_id={app_id}&app_key={app_key}')
    data = result.json()
    return data['hits']

def processString(s):
    """Processes string by escaping single and double quotation marks."""
    return s.replace("'", "\'\'").replace("\"", "\"\"")

recipeNameField = "label"

# All fields we want except for ingredients and image
requiredFields = [
    "url",
    "healthLabels",
    "calories",
    "totalTime",
    "cuisineType"
]

ingredientsFieldName = "ingredients"

# All fields we want except for food
ingredientsRequiredFields = [
    "quantity",
    "measure",
    "foodId"
]

# Returns dictionary in JSON format containing recipes corresponding to each
# keyword
def searchRecipes(keyword, count):
    retVal = {}
    results = getAPIrecipes(keyword, count)
    keywordRecipes = {}
    for recipe in results:
        recipe = recipe['recipe']

        curRecipe = {}
        recipeName = processString(recipe[recipeNameField])

        # API can return same recipes with different capitalization, so this
        # filters those out.
        if recipeName.lower() in [k.lower() for k in keywordRecipes.keys()]:
            continue

        for field in requiredFields:
            rawValue = recipe[field]
            if field == "calories":
                rawValue = int(rawValue)
            elif field == "cuisineType":
                rawValue = rawValue[0]
            curRecipe[field] = rawValue
        
        with open("images/imageCounter.txt", "r+") as f:
            imageName = int(f.read())
            f.seek(0)
            f.write(str(imageName + 1))
        imageURL = recipe["image"]
        imageData = requests.get(imageURL).content
        with open(f"images/{imageName}.jpg", "wb") as f:
            f.write(imageData)
        curRecipe["imageName"] = f"{imageName}.jpg"

        ingredients = []
        alreadyAddedIngredientNames = []
        # This is assuming the ingredients for each recipe are returned as
        # an array
        for ingredient in recipe[ingredientsFieldName]:
            # API can return same ingredient multiple times, so this filters
            # duplicate ingredients out. This doesn't catch all duplicate
            # ingredients as the same ingredient can be named differently
            # (e.g. 'cooking oil' and 'oil').
            ingredientName = processString(ingredient["food"].lower())
            if ingredientName in alreadyAddedIngredientNames:
                continue
            else:
                alreadyAddedIngredientNames.append(ingredientName)

            curIngredient = {}            
            curIngredient["food"] = ingredientName
            for field in ingredientsRequiredFields:
                curIngredient[field] = ingredient[field]
            ingredients.append(curIngredient)
        curRecipe[ingredientsFieldName] = ingredients
        keywordRecipes[recipeName] = curRecipe
    retVal[keyword] = keywordRecipes
    return retVal
