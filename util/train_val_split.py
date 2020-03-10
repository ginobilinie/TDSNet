import os
from pathlib import Path
import glob
from util.config import *

def get_split(fold):
    
    folds = {0: ['seq_1', 'seq_2', 'seq_3', 'seq_4']}
    train_file_names = []
    val_file_names = []
    ids = os.listdir(cropped_train_path)
    
    for instrument_id in ids:
        if instrument_id in folds[fold]:
            val_file_names += list((cropped_train_path / (instrument_id) / 'images').glob('*'))
        else:
            train_file_names += list((cropped_train_path / (instrument_id) / 'images').glob('*'))

    return train_file_names, val_file_names
