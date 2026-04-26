# Decoding Methods for Large Scale Models - A Comprehensive Study

Language generation is the process of generation of text from transformers based language models and it can be solved using different decoding methods like Top-k, Top-N and Beam Search etc.  Our aim for this study will be to explore the comprehensive study from foundational to the cutting edge methods in the industry and research community.

Let's understand the problem of interest. Consider the our text dataset to be a collection of sequence of $T$ tokens as $W = (w_1, w_2, ..., w_T)$ and the goal of transformer architecture is to model the probability distribution of these tokens as 

$$
P(W) = P(w_1, w_2, \dots, w_T)
$$

. We know that due to large sczmale dataset we have large scale probability distribution, which is a problem for the current hardware and algorithms. Therefore by

**chain rule of probability**, this large scale joint probability distribution can be decomposed into a product of conditional probabilities as

$$
P(W) = P(w_1, w_2, \dots, w_T) = \prod_{t=1}^{T} P(w_t | w_{1:t-1})
$$


Where, 

$P(w_t | w_{1:t-1})$

 is the conditional probability of the current token given all the previous tokens.

Remark : $w_{1:t-1}$ represents the prefix/context history.

How does transformer achitecture able to compute such multiple conditional probabilies for each token of the text data ?

The transformer achitecture consists of two parts namely encoder and decoder. If we look at the decoder only architecture that can be used to model our products of probabilities distribution using causal masking i.e addition of the look-ahead mask with the self-attention mechanism that dictates that $w_t$ can only depend on the $w_{1:t-1}$ which actually prevent that model from cheating by looking at future tokens during pre-training. For each position $t$, model produces a vector of logits $h_t$ that passes through the softmax function to turn it into the probability distribution over entire vocabulary |$V$|.

$$
P(w_t = v | w_{1:t-1}) = \frac{\exp(h_{t,v})}{\sum_{j=1}^{|V|} \exp(h_{t,j})}
$$

Now we compute the loss function/log-likelihood function during each next token prediction using cross entropy function. 

$$
\mathcal{L} = -\sum_{t=1}^{T} \log P(w_t | w_{1:t-1})
$$

and optimize this objective function during pre-training to maximize the log-likelihood of sequence of tokens.

Now if we look at encoder architecture based models like BERT that uses the Masked Language Modeling(MLM) approach

$$
P(w_{mask} | w_{context \setminus mask})
$$

which actually not only look at the past but also the future tokens by looking left and right from the current token in the sequence.

### Summary

LLM are just the probability distribution from which we can sample the data from it. We learn text data distribution during the llms transformer architecture training and save the learned weight matrix of the model and perform the sampling from the data distribution using the model inferencing.
