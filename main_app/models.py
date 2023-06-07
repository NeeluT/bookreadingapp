from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


AGE_GROUP = (
  ('A', '0-3 Months'),
  ('B', '3-6 Months'),
  ('C', '6-12 Months'),
  ('D', '1-3 Years'),
  ('E', '3-7 Years'),
  ('F', '7-13 Years'),
)


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300,default='Description')
    description = models.CharField(max_length=300, default='Description')
    age_group = models.CharField(
        max_length=1,
        choices=AGE_GROUP,
        default=AGE_GROUP[0][0])


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return (reverse('books_detail', kwargs={'book_id': self.id})or reverse('add_review', kwargs={'book_id': self.id}))


class Child(models.Model):
    name = models.CharField(max_length=100)
    # age_group = models.CharField(
    #     max_length=1,
    #     choices=AGE_GROUP,
    #     default=AGE_GROUP[0][0]
    # )
    age_group = models.IntegerField()
    books = models.ManyToManyField(Book)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        AGE_GROUP

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'child_id': self.id})
    
    def __str__(self):
        return f"{self.get_age_group_display()}"
    
class Review(models.Model):
    review = models.CharField(max_length=1000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
      

    def __str__(self):
        return f"review={self.review} id={self.id}"  
    def get_absolute_url(self):
        return reverse('add_review', kwargs={'book_id': self.id})

     
    

    



    


