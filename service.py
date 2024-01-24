from model import Model


class Service:
    def __init__(self):
        self.bart = Model("slauw87/bart_summarisation")
        self.distilbart = Model("Falconsai/text_summarization")
        self.t5_small = Model("sshleifer/distilbart-cnn-12-6")

    def get_summary_bart(self, text: str):
        return self.bart.get_summary(text)

    def get_summary_distilbart(self, text: str):
        return self.distilbart.get_summary(text)

    def get_summary_t5_small(self, text: str):
        return self.t5_small.get_summary(text)
