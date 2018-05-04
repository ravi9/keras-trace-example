import keras
import numpy as np

def predict_fn(model, run_metadata):
    img = np.random.rand(1, 28, 28, 1)
    model.predict(img)
    """
    Save the training timeline
    """
    from tensorflow.python.client import timeline

    timeline_filename = "./timeline_trace.json"
    fetched_timeline = timeline.Timeline(run_metadata.step_stats)
    chrome_trace = fetched_timeline.generate_chrome_trace_format()
    with open(timeline_filename, "w") as f:
    	print("Saved Tensorflow trace to: {}".format(timeline_filename))
    	print("To view the trace:\n(1) Open Chrome browser.\n"
    	"(2) Go to this url -- chrome://tracing\n"
    	"(3) Click the load button.\n"
    	"(4) Load the file {}.".format(timeline_filename))
    	f.write(chrome_trace)
