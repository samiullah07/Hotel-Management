from django.db import models
import uuid
# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
class Amenities(BaseModel):
    amenity_names = models.CharField(max_length=100)

    def __str__(self):
        return self.amenity_names


class Hotel(BaseModel):
    hotel_name= models.CharField(max_length=200)
    amenity = models.ManyToManyField(Amenities)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()
    banner_img = models.ImageField(upload_to="hotel_images")

    def get_Amenities(self):
       payload = []

       for obj in self.amenity.all():
           payload.append({
               "id" : obj.id,
               "amenity_names" : obj.amenity_names,
           })

        
       return payload



    def __str__(self):
        return self.hotel_name


class HotelImages(BaseModel):
    hotel = models.ForeignKey(Hotel,related_name="all_hotel", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="hotel_images")
