# Software: `softwares/recipe_creator`

This promptware is used to create a recipe from a list of ingredients.

```python
import promptware
software = promptware.install("recipe_creator")
output = software.execute("Frito Pie\n\nIngredients:\nFritos\nChili\nShredded cheddar cheese\nSweet white or red onions, diced small\nSour cream\n\nInstructions:")
# output:
# 1. Preheat oven to 350 degrees F.
# 
# 2. Spread a layer of Fritos in the bottom of a 9x13 inch baking dish.
# 
# 3. Top with chili and spread evenly.
# 
# 4. Sprinkle shredded cheese over chili.
# 
# 5. Add diced onions over cheese.
# 
# 6. Bake in preheated oven for 20 minutes.
# 
# 7. Remove from oven and top with a dollop of sour cream.
# 
# 8. Serve and enjoy!
```