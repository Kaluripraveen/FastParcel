from django.contrib import admin,messages
from django.conf import settings
from paypalrestsdk import configure,Payout

from .models import *
import random
import string


configure({
    "mode":settings.PAYPAL_MODE,
    "client_id":settings.PAYPAL_CLIENT_ID,
    "client_secret":settings.PAYPAL_CLIENT_SECRET,
})

def payout_to_courier(modeladmin,request,queryset):
    payout_items = []
    transaction_querysets = []
    #get all valid courier in queryset
    for courier in queryset:
        if courier.paypal_email:
            courier_in_transactions= Transaction.objects.filter(
                job__courier = courier,
                status = Transaction.IN_STATUS
            )

            if courier_in_transactions:
                transaction_querysets.append(courier_in_transactions)
                balance = sum(i.amount for i in courier_in_transactions)
                payout_items.append({
                            
                    "recipient_type": "EMAIL",
                    "amount": {
                        "value": "{:.2f}".format(balance*0.8),
                        "currency": "INR"
                    },
                    "receiver":courier.paypal_email,
                    "note": "Thank you.",
                    "sender_item_id": str(courier.id)
                })
    # send payout batch nd email to receivers
    
    sender_batch_id = ''.join(random.choice(string.ascii_uppercase) for i in range(12))
    payout = Payout({
        "sender_batch_header": {
        "sender_batch_id": sender_batch_id,
        "email_subject": "You have a payment"
    },
    "items": payout_items
    })
    
    #update transactions
    try:
        if payout.create():
            for i in transaction_querysets:
                i.update(status= Transaction.OUT_STATUS)
            messages.success(request,"payout[%s] created successfully"%(payout.batch_header.payout_batch_id))
        else:
            messages.error(request,payout.error)
    except Exception as e:
        messages.error(request,str(e))
class CourierAdmin(admin.ModelAdmin):
    list_display = ['user_full_name','paypal_email','balance']
    actions = [payout_to_courier]
    def user_full_name(self,obj):
        return obj.user.get_full_name()
    
    def balance(self,obj):
            
        return round(sum( t.amount for t in Transaction.objects.filter(job__courier=obj,status=Transaction.IN_STATUS))*0.8,2)
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['stripe_payment_intent_id','job','courier_paypal_email','customer','courier','amount','status','created_at']
    list_filter = ['status']
# Register your models here.
    def customer(self,obj):
        return obj.job.customer
    
    def courier(self,obj):
        return obj.job.courier
    
    def courier_paypal_email(self,obj):
        return obj.job.courier.paypal_email if obj.job.courier else None
        
admin.site.register(Customer)
admin.site.register(Courier,CourierAdmin)
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Transaction,TransactionAdmin)

