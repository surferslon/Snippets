# Cохранение бинарных данных в поле модели
import io
from django.core.files import File as DjangoFile
img_data = image['image']['text'] # бинарные данные в base64
file_name = image['name']
image_buffer = io.BytesIO()
image_buffer.write(img_data.decode('base64'))
model_with_image = WarrantyCaseImage(warranty_case=serializer.instance)
model_with_image.image.save(file_name, DjangoFile(image_buffer))
model_with_image.save()
image_buffer.close()