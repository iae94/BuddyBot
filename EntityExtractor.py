import re

class EntityExtractor:

    def __init__(self):
        self.methods = [f for f in dir(self) if re.findall(r'^_[a-zA-Z_]*', str(f))]

    def extract(self, *args, **kwargs):

        methods = kwargs.get('methods', list(set([str(s).split('_')[-1] for s in self.methods])))
        text = kwargs['text']

        result = {}
        for m in methods:
            submethods = [sm for sm in self.methods if m in sm]
            subresult = {str(sm).replace('_get_', ''): getattr(self, sm)(text) for sm in submethods}
            result[m] = subresult

        return result


    def _get_remedy_name(self):
        pass
    def _get_homer_name(self):
        pass
    def _get_mobile_phone(self):
        pass
    def _get_office_phone(self):
        pass
    def _get_date(self):
        pass

    def _get_raw(self, text):
        return text



