import csv
import datetime
import click


blood_sugar = click.prompt("Blood Sugar", type=click.INT)
weight = click.prompt("Weight", type=click.FLOAT)
insulin_units = click.prompt("Insulin_units", type=click.FLOAT)
food = click.prompt("Cans fed per day", type=click.FLOAT)
date = datetime.date.today()

with open('ramabg.csv', 'a', newline='') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(
		[
			date,
			blood_sugar,
			weight,
			insulin_units,
			food
		]
	)
	

