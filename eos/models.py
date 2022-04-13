from django.db import models

class Book(models.Model):
   ISBN = models.CharField(primary_key=True, max_length=20)
   title = models.CharField(max_length = 100,null=True)
   summary = models.CharField(max_length = 1000,null=True)
   numberOfPage = models.IntegerField(null=True)
   language = models.CharField(max_length=20,null=True)
   img = models.ImageField()
   publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE)
   category = models.ForeignKey("Category",on_delete=models.CASCADE)
   author = models.ForeignKey("Author",on_delete=models.CASCADE)
   class Meta:
      db_table = "book"

class Publisher(models.Model):
   name = models.CharField(max_length = 100,null=True)
   address = models.CharField(max_length = 100,null=True)
   class Meta:
      db_table = "publisher"

class Category(models.Model):
   name = models.CharField(max_length = 100,null=True)
   createdAt = models.DateField(auto_now=True)
   class Meta:
      db_table = "category"

class Author(models.Model):
   name = models.CharField(max_length = 100,null=True)
   biography = models.CharField(max_length = 100,null=True)
   class Meta:
      db_table = "author"

class BookItem(models.Model):
   barcode = models.CharField(max_length = 100,null=True)
   price = models.FloatField()
   discount = models.FloatField()
   book = models.ForeignKey("Book",on_delete=models.CASCADE)
   class Meta:
      db_table = "bookitem"

class BookStats(models.Model):
   quantity = models.IntegerField()
   importPrice = models.FloatField()
   quantityLeft = models.IntegerField()
   book = models.ForeignKey("Book",on_delete=models.CASCADE)
   class Meta:
      db_table = "bookstats"