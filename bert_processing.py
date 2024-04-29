import torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler
from transformers import BertTokenizer, BertModel

def prepare_bert_inputs(sentences):
    # Instantiate BERT tokenizer and model
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    bert_model = BertModel.from_pretrained('bert-base-uncased')

    # Tokenize sentences and pad sequences
    inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

    # Get input IDs and attention masks
    input_ids = inputs["input_ids"]
    attention_masks = inputs["attention_mask"]

    return input_ids, attention_masks, tokenizer, bert_model

def process_bert_outputs(input_ids, attention_masks, bert_model):
    # Define batch size and create DataLoaders
    batch_size = 32
    train_data = TensorDataset(input_ids, attention_masks)
    train_sampler = RandomSampler(train_data)
    train_dataloader = DataLoader(train_data, sampler=train_sampler, batch_size=batch_size)

    outputs_all = []

    # Model forward pass
    for batch in train_dataloader:
        batch_input_ids, batch_attention_masks = batch
        outputs = bert_model(input_ids=batch_input_ids, attention_mask=batch_attention_masks)
        outputs_all.append(outputs)

    return outputs_all
