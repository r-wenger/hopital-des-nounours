from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import csv
from os.path import join

path_template = "diplome_nounours.jpg"
path_folder_parent = 'export'

with open('liste.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		msg = row['Prenom'] + ' ' + row['Nom']
		path_export = join(path_folder_parent, row['Prenom'] + '_' + row['Nom'] + '.jpg')

		img = Image.open(path_template)
		draw = ImageDraw.Draw(img)
		W, H = img.size
		font = ImageFont.truetype("Forum-Regular.otf", 70, encoding="utf-8")
		w, h = draw.textsize(msg, font=font)
		draw.text(((W-w)/2,(H-h)/2), msg, (0,0,0), font=font)
		img.save(path_export)