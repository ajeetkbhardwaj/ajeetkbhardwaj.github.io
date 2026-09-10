# LLM Inference Engine In MLX - AnLLM

![1788869236726](image/anllm/1788869236726.png)

In any transformer based large scale models specially llms, there are two operation are the core of entire architecture 

1. Matrix Matrix Multiplication
2. Matrix Vector Multiplication

While matrix matrix multiplication exist almost everywhere but only during inference time we se the matrix vector multiplication to serve inference to the users query.

The entire lifecycle of the the large scale models can be divided into two parts

1. LSM Building
2. LSM Serving

As, we know the most of the lsm are based onto the transformer architecture, so thier building phase can be subdivided into the 

1. Pretraining : We Train our LSM onto the Large Scale Datasets like entire internet over history of time. Then model become generalized enough for many tasks
2. Post-training : We needed to make it align with the human how they do any real tasks via postraining onto specific types of datasets and environments.

Now, comes the real part how to save and export the model for doing inferences. There are many inference engines are build for specific devices like llama.cpp focus onto cpu/edge devices that accepts the GGUF format of model while vLLM, TensorRT and other that are GPU specialized to serve inference in distributed setup at large scale requires the model export format like AWQ etc.

Thus, question comes infront of use is to how to build inference engine like llama.cpp or vLLM from scratch so this is the journey that i had gone and i had also curated a list of tutorials that might help you to navigate your journey to build an llm inference engine using mlx.
