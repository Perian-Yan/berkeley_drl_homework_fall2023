from tensorboard.backend.event_processing import event_accumulator
import numpy as np

def load_tfevents(log_dir, tags):
    event_data = event_accumulator.EventAccumulator(log_dir)
    event_data.Reload()
    
    data = {}
    for tag in tags:
        tag_array = []
        for event in event_data.Scalars(tag):
            tag_array.append(event.value)
        data[tag] = np.array(tag_array)
    return data