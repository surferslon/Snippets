
class DataRemovingView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'admin/data_remove.html',
            {
                'objects_formset': RemovableObjectsFormset(
                    initial=[{'app': app, 'model': model} for app, model in settings.CLEANABLE_MODELS]
                )
            }
        )