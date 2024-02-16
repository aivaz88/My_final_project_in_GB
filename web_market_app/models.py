from django.db import models


class UserStatus(models.Model):
    type = models.CharField(max_length=128)
    name = models.CharField(max_length=128)


class User(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    telephone = models.CharField(max_length=14)
    email = models.EmailField()
    password_hash = models.CharField(max_length=128)
    reg_date = models.DateTimeField(auto_now_add=True)
    links_media = models.TextField()
    avatar = models.ImageField(upload_to='static/img/avatars/')
    status_id = models.ForeignKey(UserStatus, on_delete=models.CASCADE, default='customer')


class Tag(models.Model):
    name = models.CharField(max_length=128)


class City(models.Model):
    name = models.CharField(max_length=128)


class Country(models.Model):
    name = models.CharField(max_length=128)


class Location(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)


class RetreatCategory(models.Model):
    name = models.CharField(max_length=128)


class RetreatPhoto(models.Model):
    image = models.ImageField(upload_to='static/img/retreats/')


class Retreat(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    category_id = models.ForeignKey(RetreatCategory, on_delete=models.CASCADE)
    photo_id = models.ForeignKey(RetreatPhoto, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    links_preview = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_stop = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    retreat_form = models.BooleanField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)

    def get_summary(self):
        words = self.description.split()
        return f'{" ".join(words[:12])}...'


class Feedback(models.Model):
    retreat_id = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(),
    rating = models.IntegerField()


class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    retreat_id = models.ForeignKey(Retreat, on_delete=models.CASCADE)


class Booking(models.Model):
    retreat_id = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    tickets_amount = models.IntegerField()
    booking_coast = models.DecimalField(max_digits=8, decimal_places=2)


class PaymentStatus(models.Model):
    status = models.CharField(max_length=15)


class Payment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    retreat_id = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    status_id = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
