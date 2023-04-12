import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from shopping.models import shopping_index

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        shopping_index.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database

        base_dir = Path(__file__).resolve().parent.parent.parent.parent

        with open(str(base_dir) + '/shopping/database/amazon_co-ecommerce_index.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                print(row)
                shopping = shopping_index.objects.create(
                    uniq_id=row[0],
                    product_name=row[1],
                    manufacturer=row[2],
                    price = float(row[3]),
                    average_review_rating = row[4],
                    country = row[5],
                )
                shopping.save()

            # else:
            # next(reader)