from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.user} Booking For {self.listing.title}"


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user} Review for {self.listing.title}"

class Payment(models.Model):
    STATUS_PENDING = "pending"
    STATUS_COMPLETED = "completed"
    STATUS_FAILED = "failed"

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tx_ref = models.CharField(max_length=100, unique=True)
    checkout_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tx_ref} - {self.status}"
