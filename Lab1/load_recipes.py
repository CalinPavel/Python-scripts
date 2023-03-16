#!/usr/bin/env python

import os

RECIPES_FOLDER = "recipes"

recipes = []

for filename in os.listdir(RECIPES_FOLDER):
	drink = {}
	if filename.endswith(".txt"):
		with open(os.path.join(RECIPES_FOLDER, filename), 'r') as file:
			for line in file:
				if '=' in line:
					fields = line.strip().split('=')

					key = fields[0].strip()
					value = int(fields[1].strip())
					drink[key] = value
				else:
					key = 'name'
					value = line.strip()
					drink[key] =value
	recipes.append(drink)