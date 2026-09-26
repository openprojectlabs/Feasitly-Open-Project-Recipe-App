# Feastly Recipe App

Feastly is a local-first recipe discovery app using a bundled 83,571-recipe collection.

## New in this version
- Large searchable recipe catalog
- Advanced ingredient, category and diet-style filtering
- Web recipe discovery without copying third-party recipe text into the local catalog
- Cook Mode for datasets that include directions
- 7-day meal planner
- Saved recipes
- Shopping-list builder
- Wikimedia Commons food-image lookup
- Dark mode
- RecipeNLG import pipeline for a much larger external dataset
- Simple Node server and health endpoint

## Run

Node:

    node server.js

Then open http://localhost:8000

Python alternative:

    python -m http.server 8000

## Add the 2.23M RecipeNLG dataset

RecipeNLG publishes a dataset of 2,231,142 recipes. Download it from the official RecipeNLG project, then run:

    python scripts/import_recipenlg.py path/to/full_dataset.csv data/recipenlg.json

The importer keeps title, ingredients, directions and source link where present. It does not scrape websites or invent missing instructions.

## External APIs

For a production version, put recipe/nutrition API credentials behind a server-side proxy. Do not put private API keys in browser JavaScript.

Useful integrations:
- Edamam Recipe Search: millions of web recipes plus filters, images and nutrition; licensed content can include cooking instructions.
- USDA FoodData Central: food and nutrient lookup.
- Spoonacular: recipe/food/nutrition API.

The current UI does not pretend these APIs are connected until credentials and a server integration are actually configured.
