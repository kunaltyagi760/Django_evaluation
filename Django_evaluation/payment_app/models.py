from django.db import models

class Service(models.Model):
    # should have type where choices: Mobile Recharge, DTH Recharge, Insurance payment, mode_of_payment where choices: UPI, internet banking, card payment, and company as fields)

    Mobile_Recharge = 'Mobile Racharge'
    DTH_Recharge = 'DTH Recharge'
    Insurance_Payment = 'Insurance Payment'
    Type_Choices = (
        (Mobile_Recharge, 'Mobile Racharge'),
        (DTH_Recharge, 'DTH Recharge'),
        (Insurance_Payment, 'Insurance Payment')
    )

    UPI = 'UPI'
    Internet_Banking = 'Internet Banking'
    Card_Payment = 'Card Payment'
    Payment_Choices = (
        (UPI, 'UPI'),
        (Internet_Banking, 'Internet Banking'),
        (Card_Payment, 'Card Payment')
    )

    type = models.CharField(max_length = 50, choices = Type_Choices, default= Mobile_Recharge)
    mode_of_payment = models.CharField(max_length = 50, choices = Payment_Choices, default=UPI)
    company = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class ServiceUser(models.Model):
    # (having name, email, age, gender as necessary fields, use field Types accordingly, Keep gender as choices/select tag)

    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
    (Male, 'Male'),
    (FeMale, 'Female'),
    )
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = Male)
    services = models.ManyToManyField(Service, related_name='service_user')

    def __str__(self):
        return self.name
    
class Subscription(models.Model):
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.IntegerField()
    current_date = models.DateTimeField(auto_now=True)







