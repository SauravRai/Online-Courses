This repository contents the learnings from the Pluralsight Tensorflow course. 

Module 1 Notes: Exploring the TensorFlow 2.0 Framework
**********************************************************
- Tensorflow 2 use of the high-level APIs with the keras has made designing and training the Neural network easier. While its eager execution mode makes prototyping and debugging models a lot easier. 
  The dynamic graph is great for prototyping.
- The expectation at the end of the course: Able to harness the computational power of the Tensorflow 2.0
- TF2x gives support for both the Dynamic and Static computation graphs.
- Pytorch makes prototyping DL models a lot easier.
- In the TF 1x, to able to execute the computation graph instantiate the session object(TF.session) and execute the graph within the session.
- A major function that these frameworks should support is to run in parallel GPUs. For example in TF1x there is tf.device and in PyTorch there is torch.nn.DataParallel to use GPUs.
- Today Keras is a central part of the tightly connected TF 2.0 ecosystem. Today the way to Tensorflow is through/using Keras
- The single major change in the TF2x is the use of the Eager execution.
