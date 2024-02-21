from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    subject = models.TextField()

    def __str__(self) :
        return self.name

class Cadidate(models.Model):
    cadidate_name = models.CharField(max_length=50)
    pdf_file = models.FileField(upload_to='pdfs/')  # Field for storing PDF files
    candidate_id = models.CharField(max_length=20)  # Field for storing candidate ID

    def __str__(self):
        return self.cadidate_name
    


    