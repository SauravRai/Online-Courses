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
- Neuron is a simple mathematical function and it operates on several x values and gives output several y values. It is shown in the following diagram as well.
- The choice of activation function is crucial in determining performance.
- In Tf2x, the computation graph that we set up is in the eager execution by default.
- All tensors are immutable like Python numbers and strings: you can never update the contents of a tensor, only create a new one.
- Tensors and numpy arrays are perfectly compatible. This means you can do numpy operations on the tensors as well but not recommended :)
- Variables are the recommended way to share the persistent state in the TensorFlow programs. Variables unlike Tensors are mutable.
- It can be thought of as a mutable container holding tensors. Tensors held by a variable can be mutated or changed by running operations on those variables.
- We can use tf.Variable invocation in order to instantiate a new variable. 

