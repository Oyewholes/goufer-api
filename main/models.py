from django.db import models
from .validate import validate_file_size
from user.models import ErrandBoy, Gofer, MessagePoster, Vendor
from django.core.validators import FileExtensionValidator


class Location(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"Gofer at {self.latitude}, {self.longitude}"

class Category(models.Model):
    CATEGORY_CHOICES = (
    ('food', 'Food'),
    ('entertainment', 'Entertainment'),
    ('transportation', 'Transportation'),
    ('tourism_and_travel', 'Tourism & Travel'),
    ('religious_donations', 'Religious Donations'),
    ('medical', 'Medical'),
    ('services', 'Services'),
    ('legal', 'Legal'), 
    ('technical', 'Technical'),
    ('employments', 'Employment'),
    ('housing', 'Housing'),
    ('real_estate', 'Real Estate'),
)
    category_name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class GoferDocument(models.Model):
    
    DOCUMENT_CHOICES = (
        ('ssn', 'SSN'),
        ('nin', 'NIN')
    )
    
    document_type = models.CharField(max_length=5, choices=DOCUMENT_CHOICES)
    document_number = models.CharField(max_length=11, unique=True)
    gofer = models.ForeignKey(Gofer, on_delete=models.CASCADE, related_name="documents" )
    document_of_expertise = models.FileField(upload_to='main/documents', validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['jpg', 'png', 'pdf'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.document_type
    
class VendorDocument(models.Model):
    
    DOCUMENT_CHOICES = (
        ('ssn', 'SSN'),
        ('nin', 'NIN')
    )
    
    document_type = models.CharField(max_length=5, choices=DOCUMENT_CHOICES)
    document_number = models.CharField(max_length=11, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="documents" )
    document_of_expertise = models.FileField(upload_to='main/documents', validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['jpg', 'png', 'pdf'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.document_type
class ErrandBoyDocument(models.Model):
    
    DOCUMENT_CHOICES = (
        ('ssn', 'SSN'),
        ('nin', 'NIN')
    )
    
    document_type = models.CharField(max_length=5, choices=DOCUMENT_CHOICES)
    document_number = models.CharField(max_length=11, unique=True)
    errand_boy = models.ForeignKey(ErrandBoy, on_delete=models.CASCADE, related_name="documents" )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.document_type
    
class Reviews(models.Model):
    message_poster = models.ForeignKey(MessagePoster, on_delete=models.CASCADE, related_name='user_reviews')
    gofer = models.ForeignKey(Gofer, on_delete=models.CASCADE, related_name='gofer_reviews')
    comment = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"This is the review of {self.reviews.gofer}"
    
class Gofer(models.Model):
    pass
    
    

 