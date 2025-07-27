import markovify
import os
import json
import pickle as pkl

MODEL_FILE = "model.pkl"

def save_markov_model(model: markovify.NewlineText) -> None:
    with open(MODEL_FILE, "wb") as f:
        pkl.dump(model, f)
        
def load_markov_model() -> markovify.NewlineText:
    with open(MODEL_FILE, "rb") as f:
        markov_model = pkl.load(f)
        return markov_model

def markov_model_is_saved() -> bool:
    if os.path.exists(MODEL_FILE):
        return True
    else:
        return False
    
def create_and_save_markov_model() -> None:
    with open(file='sentences.json', mode='r', encoding='utf-8') as file:
        SENTENCES = json.load(file)
        MARKOV_MODEL = markovify.NewlineText("\n".join(SENTENCES))
        save_markov_model(MARKOV_MODEL)

def get_markov_model() -> markovify.NewlineText:
    if not markov_model_is_saved():
        create_and_save_markov_model()
    return load_markov_model()
