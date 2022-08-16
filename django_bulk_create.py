count = 0
mdl_to_save = []
for mdl_id, mdl_props in models.items():
    if mdl_props['loaded']:
        continue
    mdl_to_save.append(VehicleModel(
        match_id=mdl_id,
        brand=VehicleBrand.objects.get(pk=mdl_props['brand_id']),
        name=mdl_props['name']
    ))
    count += 1
    if count % 100 == 0:
        VehicleModel.objects.bulk_create(mdl_to_save)
        mdl_to_save = []
VehicleModel.objects.bulk_create(mdl_to_save)