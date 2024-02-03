from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

SIZE_5_MB = 5 * 1024 * 1024

# class MaxFileSizeValidator(BaseValidator):
#     def clean(self, x):
#         return x.size
#
#     def compare(self, file_size, max_size):
#         return max_size < file_size

def validate_file_size(value):
    if value.size > SIZE_5_MB:
        raise ValidationError('Image size must be no more than 5 MB.')
