from rest_framework import serializers

from store.models import Online, C2BPayments


class OnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Online
        fields = ("id",)


class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = ("id",
                  "TransactionType",
                  "TransID",
                  "TransTime",
                  "TransAmount",
                  "BusinessShortCode",
                  "BillRefNumber",
                  "InvoiceNumber",
                  "OrgAccountBalance",
                  "ThirdPartyTransID",
                  "MSISDN",
                  "FirstName",
                  "MiddleName",
                  "LastName",
                  )
