from django.db import models

# Create your models here.
class PatentDatabase(models.Model):
    Application_Number = models.BigIntegerField(primary_key=True, verbose_name='Application Number')
    Application_Type = models.TextField(null=True, verbose_name='Application Type')
    Date_of_Publication = models.TextField(null=True, verbose_name='Date of Publication')
    Title_of_Invention = models.TextField(null=True, verbose_name='Title of Invention')
    Field_of_Invention = models.TextField(null=True, verbose_name='Field of Invention')
    E_Mail = models.TextField(null=True, verbose_name='E-Mail')
    Alternate_E_Mail = models.TextField(null=True, verbose_name='Alternate E-Mail')
    Request_Examination_Date = models.TextField(null=True, verbose_name='Request Examination Date')

    class Meta:
        db_table = 'public.patent_database'
        verbose_name_plural = 'Patent Database'

    def __str__(self):
        return f"{self.Application_Number} - {self.Title_of_Invention}"
