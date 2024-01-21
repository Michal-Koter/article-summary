from model import Model


class Service:
    def __init__(self):
        self.bart = Model("slauw87/bart_summarisation")
        self.destilbart = Model("Falconsai/text_summarization")
        self.t5_small = Model("sshleifer/distilbart-cnn-12-6")

    def get_summary(self, text: str):
        result = dict()

        result['bart'] = self.bart.get_summary(text)
        result['destilbart'] = self.destilbart.get_summary(text)
        result['t5_small'] = self.t5_small.get_summary(text)

        return result

    def get_summary_bart(self, text: str):
        return self.bart.get_summary(text)

    def get_summary_destilbart(self, text: str):
        return self.destilbart.get_summary(text)

    def get_summary_t5_small(self, text: str):
        return self.t5_small.get_summary(text)
