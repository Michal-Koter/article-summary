import model


class Service:
    def __init__(self):
        self.bert = model.Bert()
        self.destilbert = model.Destilbert()
        self.t5_small = model.T5Small()

    def get_summary(self, text: str):
        result = dict()

        result['bert'] = self.bert.get_summary(text)
        result['destilbert'] = self.destilbert.get_summary(text)
        result['t5_small'] = self.t5_small.get_summary(text)

        return result

    def get_summery_bart(self, text: str):
        return self.bert.get_summary(text)

    def get_summery_destilbert(self, text: str):
        return self.destilbert.get_summary(text)

    def get_summery_t5_small(self, text: str):
        return self.t5_small.get_summary(text)
