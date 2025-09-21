import markovify
import os
import json
import pickle as pkl
import pathlib

MODEL_FILE = "markov_model.pkl"
SENTENCES_FILE = "sentences.json"


def save_markov_model(model: markovify.NewlineText) -> None:
    with open(MODEL_FILE, "wb") as file:
        pkl.dump(model, file)


def load_markov_model() -> markovify.NewlineText:
    with open(MODEL_FILE, "rb") as file:
        markov_model = pkl.load(file)
        return markov_model


def markov_model_is_saved() -> bool:
    if os.path.exists(MODEL_FILE):
        return True
    else:
        return False


def delete_markov_model() -> bool:
    if pathlib.Path(MODEL_FILE).exists():
        os.remove(MODEL_FILE)
        return True
    return False


def create_and_save_markov_model() -> None:
    try:
        with open(file=SENTENCES_FILE, mode='r', encoding='utf-8') as file:
            SENTENCES = json.load(file)

        if not SENTENCES:
            raise ValueError(f"The file {SENTENCES_FILE} is empty or contains no valid sentences.")

        if len(SENTENCES) < 10:
            raise ValueError(f"The file {SENTENCES_FILE} contains only {len(SENTENCES)} sentences. "
                             "You need at least 10 sentences for decent haiku generation.")

        MARKOV_MODEL = markovify.NewlineText("\n".join(SENTENCES))
        save_markov_model(MARKOV_MODEL)

    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find {SENTENCES_FILE}.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {SENTENCES_FILE}: {e}")
    except Exception as e:
        raise RuntimeError(f"Error creating Markov model: {e}")


def get_markov_model() -> markovify.NewlineText:
    try:
        if not markov_model_is_saved():
            create_and_save_markov_model()
        return load_markov_model()
    except Exception as e:
        raise RuntimeError(f"Error loading Markov model: {e}")
