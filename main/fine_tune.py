from transformers import AutoModelForCausalLM , AutoTokenizer , BitsAndBytesConfig
import torch

def get_model_and_tokenizer(pretrained_model_path , use_4bit , bnb_4bit_compute_dtype , bnb_4bit_quant_type , use_nested_quant , device_map):

    compute_type = getattr(torch , bnb_4bit_compute_dtype)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=use_4bit,
        bnb_4bit_quant_type=bnb_4bit_quant_type,
        bnb_4bit_compute_dtype=compute_type,
        bnb_4bit_use_double_quant=use_nested_quant
    )

    model = AutoModelForCausalLM.from_pretrained(
        pretrained_model_name_or_path=pretrained_model_path,
        quantization_config = bnb_config,
        device_map = device_map
    )

    model.config.use_cache = False
    model.config.pretraining_tp = 1

    tokenizer = AutoTokenizer.from_pretrained(
        pretrained_model_name_or_path=pretrained_model_path,
        padding_side='right',
        trust_remote_code=True
    )

    tokenizer.pad_token = tokenizer.eos_token

    return model , tokenizer