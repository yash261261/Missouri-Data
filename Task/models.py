from django.db import models
import dateutil.parser

# Create your models here.

class MissouriData(models.Model):
    county = models.IntegerField(null=True)
    est_name  = models.CharField(max_length=200,null=True)
    est_addr = models.CharField(max_length=500,null=True)
    est_city = models.CharField(max_length=200,null=True)
    est_state = models.CharField(max_length=100,null=True)
    est_zip = models.IntegerField(null=True)
    est_number = models.CharField(max_length=200,null=True)
    app_apr_code = models.CharField(max_length=100,null=True)
    date_lic = models.DateField(null=True)
    
# Validate rows

    def clean_fields(self, exclude=None):
        if not isinstance(self.est_name, str):
            self.est_name = None
        if not isinstance(self.est_addr, str):
            self.est_addr = None
        if not isinstance(self.est_city, str):
            self.est_city = None
        if not isinstance(self.est_state, str):
            self.est_state = None
        if not isinstance(self.est_number, str):
            self.est_number = None
        if not isinstance(self.app_apr_code, str):
            self.app_apr_code = None

        try:
            self.county = int(self.county)
        except:
            self.county = None
        try:
            self.est_zip = int(self.est_zip)
        except:
            self.est_zip = None
        try:
            self.date_lic = dateutil.parser.parse(self.date_lic).date()
        except:
            self.date_lic = None


    def __str__(self):
        #return f'{self.county} {self.est_name}'  # This format works in Pythono3
        return '{county} {est_name}'.format(county=self.county, est_name=self.est_name)

