from datasets import load_dataset
from datasets.dataset_dict import DatasetDict

from DataProcessor import DataProcessor


class VicunaDataProcessor(DataProcessor):
    def __init__(self, config, tokenizer):
        self.config = config
        self.tokenizer = tokenizer

    def get_data(self) -> DatasetDict:
        if "model_context_window" in self.config:
            context_window = self.config["model_context_window"]
        else:
            context_window = self.tokenizer.model_max_length

        data = load_dataset('json', data_files=self.config["data"]["dataset"]) # , split='train')
        data = data.map(lambda data_point: self.tokenizer(
            self._generate_prompt(
                data_point["conversations"],
                self.tokenizer.eos_token),
            max_length=context_window,
            truncation=True,
            padding='max_length',
        ))
        return data

    def _generate_prompt(self, convo: list, eos_token: str) -> str:
        convo_text = ""
        for turn in convo:
            entity = turn["from"]
            value = turn["value"]

            if entity == "system":
                convo_text += self.config["data"]["system_header"]  # e.g. "### SYSTEM:\n"
                end_token = ""
            elif entity == "human":
                convo_text += self.config["data"]["user_header"]  # e.g. "### HUMAN:\n"
                end_token = ""
            elif entity == "gpt":
                convo_text += self.config["data"]["response_header"]  # e.g. "### RESPONSE:\n"
                end_token = eos_token  # LLM should stop its output after the response
            else:
                print(f"WARNING: unknown entity {entity}")
                convo_text += f"### {entity.upper()}:\n"
                end_token = ""

            convo_text += value + end_token + "\n\n"
        return convo_text
