# keras-trace-example

Run the following:
```
python mnist_train.py   
python mnist_inference.py 
```
This will save Tensorflow trace to: ./timeline_trace.json                                                                                                                                                                           
To view the trace:                                                                                                                                                                                                         
(1) Open Chrome browser.                                                                                                                                                                                                   
(2) Go to this url -- chrome://tracing                                                                                                                                                                                     
(3) Click the load button.                                                                                                                                                                                                 
(4) Load the file ./timeline_trace.json
