24/11/2025
***********
Transformer architecture 
https://jalammar.github.io/illustrated-transformer/
https://jalammar.github.io/
https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/

Vector Database links
https://spacy.io/usage/embeddings-transformers
https://platform.openai.com/docs/guides/embeddings

Transfomer can be trained parallelly which was one of the drawbacks of the RNN network. 
LLM is also called as the universal solver. 
There are variants of encoder and decoder models. BERT is just the encoder and GPT models are just the decoder. 

29/11/2025
***********
Embeddings: In the context of Large Language Models (LLMs), embeddings are high-dimensional vectors that represent words, sentences, or other textual data points, capturing their semantic meaning and relationships in a continuous space for use in tasks like language understanding, generation, and similarity matching.
- Embeddings do not only require direction; they also capture both magnitude and direction in their vector representations.
- Context is most important in word embeddings
- There are Word embeddings and then later => Sentence embeddings
- word embeddings -> [Decoder] -> sentence embeddings
- There are 2 distance metrics to measure the similarity 
  (1) Euclidean distance: small value points are close in space. 
  (2) Cosine similarity: near 1.0 are same direction means similar meaning.
- Multimodal models are designed to handle multiple types of data (such as text, audio, images, etc.) simultaneously. These models are capable   of processing, understanding, and generating information that spans more than one modality of data. They learn from diverse input sources and can create connections or insights that bridge those different types of information.


1. Vector DB is the place where we store embeddings. 
2. What is Langchain? 
- LangChain is an open-source framework designed to make it easier to build applications powered by large language models (LLMs) such as GPT. 
It provides tools, abstractions, and integrations that help developers connect LLMs with:
    External data (files, databases, APIs)
    Reasoning tools (search engines, code execution, agents)
    Application logic (chains, workflows)

- Components to build the production grade application. 
- Example: Models are like car engine, but programmers need APIs/connectivity to interact with models and data. That framework is called as
  Langchain.
- Unified interface like Hugging face where you can find everything like different models for different applications and everything. Single place to get
  everything.
- LLMS gives you output distributions and it does sampling operation so the responses are always varying. Temperature parameter value if it more than 0 then the
  responses are more dynamic and not static.
     

Link to the langchain 
https://www.langchain.com/
langchain_openai is the package that connects the Langchain framework with OpenAi's models and services for building AI applications.

3. Alternative to Langchain is:
   llmaindex
   https://www.llamaindex.ai/
   semantic kernel from microsoft azure 
   https://learn.microsoft.com/en-us/semantic-kernel/overview/
   autogen from microsoft 
   https://microsoft.github.io/autogen/stable//index.html
   
Tensorflow playground: 
A nice tool to visualise the impact of each of the parameters and hyperparameters. 
Just type tensorflow playground


30/11/2025:
***********
- 


