# from django.db import models
# from djongo import models
#
#
# # Create your models here.
#
# class restricted(models.Model):
#     name = models.CharField(max_length=50, default="N/A")
#
# #class name should be capitals, but using existing file where names are in lower case.
# class retailer(models.Model):
#     name = models.CharField(max_length=50, default="N/A")
#     restricted = models.ArrayModelField(
#         model_container=restricted,
#     )
#
#
# class comments(models.Model):
#     comment_country = models.ForeignKey(restricted, on_delete=models.CASCADE)
#     comment_retailer = models.ForeignKey(retailer, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=50, default="N/A")
