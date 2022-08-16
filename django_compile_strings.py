
from django.db.models.functions import Concat
from django.db.models import F, Value, CharField

existing_doctors = Doctor.objects.all().annotate(
    full_name=Concat(
        F('user__last_name'),
        Value(' '),
        F('user__first_name'),
        Value(' '),
        F('user__middle_name'),
        output_field=CharField()
    )
)