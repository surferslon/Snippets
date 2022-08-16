# making list from m2m and m2o fields

from django.contrib.postgres.aggregates import ArrayAgg

Model.objects.filter().annotate(subways_list=ArrayAgg('subway__title')

# improved:
Model.objects.filter()).annotate(subways_list=ArrayAgg('subway__title', distinct=True, filter=Q(subway__title__isnull=False)),