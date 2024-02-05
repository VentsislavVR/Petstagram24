# class DisabledFormMixin:
#     disabled_fields = ()
#     fields = {}
#
#     def _disable_fields(self):
#         if self.disabled_fields == '__all__':
#             fields = self.fields.keys()
#         else:
#             fields = self.disabled_fields
#
#         for field_name in fields:
#             if field_name in self.fields:
#                 field = self.fields[field_name]
#                 # field.widget.attrs['disabled'] = 'disabled'
#                 field.widget.attrs['readonly'] = 'readonly'


class ReadonlyFieldsFormMixin:
    readonly_fields = ()

    def _apply_readonly_on_fields(self):
        for field_name in self.readonly_field_names:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"

    @property
    def readonly_field_names(self):
        if self.readonly_fields == "__all__":
            return self.fields.keys()

        return self.readonly_fields
