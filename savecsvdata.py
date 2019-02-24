"""
Migrate csv data into Django Database
"""
import csv
import os

from django.core.exceptions import ValidationError

dir_path = os.path.dirname(os.path.realpath(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HealthApplication.settings")

from Task.models import MissouriData

with open('MissouriData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    imported, count = 0, 0
    for row in reader:
        count+=1
        try:
            p = MissouriData(county=row['County'], est_name=row['Establishment Name'],
                             est_addr=row['Establishment Address'],
                             est_city=row['Establishment City'], est_state=row['Establishment State'],
                             est_zip=row['Establishment Zip Code'],
                             est_number=row['Telephone Number'], app_apr_code=row['Application Approval Code'],
                             date_lic=row['Date Licensed'])
            p.full_clean()
            p.save()
            imported+=1
        except ValidationError as e:
            print("Could not process data:", row, e)
            pass

    print ("Migration Completed. Total {} | Imported {}".format(count, imported))
