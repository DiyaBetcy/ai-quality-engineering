
# LLM Fundamentals

## 1. Introduction to Large Language Models

A Large Language Model (LLM) is an AI model trained on
large amounts of text data to understand and generate
human-like language.

LLMs can perform tasks such as:

- Answering questions
- Summarizing documents
- Generating content
- Translating languages
- Writing and explaining code
- Following natural-language instructions

Examples include GPT, Gemini, Claude and Llama.

## 2. How Does an LLM Work?

At a high level, an LLM:

1. Receives an input prompt.
2. Processes the input as tokens.
3. Uses its learned patterns to predict the next token.
4. Generates an output token by token.
5. Continues until it reaches a stopping condition.

LLMs generate responses based on learned patterns.
They do not guarantee that every generated statement
is factually correct.

## 3. Prompts

A prompt is the instruction or input given to an LLM.

Example:

```text
Explain software testing in simple language.
```

### Types of Prompts

**Zero-shot prompting**

Giving an instruction without providing examples.

Example:

```text
Classify this review as positive or negative:
"The application is easy to use."
```

**One-shot prompting**

Providing one example before asking the model to perform a task.

**Few-shot prompting**

Providing multiple examples to guide the model's response.

### Importance of Prompt Quality

A good prompt should provide:

- Clear instructions
- Relevant context
- Expected output format
- Necessary constraints

## 4. Tokens

Tokens are smaller units of text processed by an LLM.

A token can represent:

- A complete word
- Part of a word
- Punctuation
- Other text units

For example, a sentence is divided into tokens
before being processed by the model.

Tokenization is important because model usage and
processing limits are often measured in tokens.

## 5. Context Window

The context window is the amount of information
an LLM can consider during a single interaction.

It may include:

- User prompts
- Previous conversation messages
- System instructions
- Retrieved documents
- Generated responses

If the available context is exceeded, some information
may be truncated or excluded.

### Testing Considerations

- Does the model remember relevant earlier instructions?
- Does it handle long inputs correctly?
- Does it lose important information in long conversations?
- Does its response remain relevant?

## 6. Temperature

Temperature controls the randomness of token selection
during response generation.

| Temperature | General behaviour |
|---|---|
| Low | More predictable and consistent |
| Medium | Balanced variation |
| High | More varied and creative |

A low temperature can be useful for factual or
structured responses.

A higher temperature may be useful for creative tasks.

Temperature does not guarantee correctness.

## 7. Inference

Inference is the process of using a trained model
to generate an output from a given input.

Example:

Input:
"Who developed Python?"

Model output:
"Python was developed by Guido van Rossum."

Inference is different from training.

- Training: Learning patterns from data.
- Inference: Using the trained model to generate responses.

## 8. Hallucinations

An LLM hallucination occurs when a model generates
information that sounds convincing but is incorrect,
unsupported or fabricated.

Example:

Question:
"Who developed Python?"

Incorrect response:
"Python was developed by James Gosling."

The answer sounds plausible but is factually incorrect.

### Why Hallucinations Occur

Possible reasons include:

- Incomplete or inaccurate learned information.
- Ambiguous prompts.
- Missing context.
- Model prediction limitations.
- Pressure to provide an answer even when uncertain.

### Testing for Hallucinations

- Ask questions with known answers.
- Provide a reference context.
- Compare the response with trusted information.
- Check whether the model invents facts.
- Test whether the model admits uncertainty.

## 9. Conventional Software Testing vs LLM Testing

| Conventional software testing | LLM testing |
|---|---|
| Often checks predefined expected outputs | Often evaluates response quality |
| Usually deterministic | Can be non-deterministic |
| Uses exact assertions frequently | May need semantic evaluation |
| Focuses on functional behaviour | Also checks relevance, faithfulness and safety |
| Failures can be reproduced consistently | Outputs may vary between runs |

Both approaches require systematic test cases,
clear requirements and measurable acceptance criteria.

## 10. Practical LLM Testing Scenarios

### Scenario 1: Factual Accuracy

Question:
"Who developed Python?"

Expected answer:
"Guido van Rossum."

Check whether the model provides the correct answer.

### Scenario 2: Instruction Following

Prompt:
"Explain Python in exactly two bullet points."

Check:

- Are there exactly two bullet points?
- Are both points relevant?
- Did the model follow the requested format?

### Scenario 3: Context-Based Answering

Context:
"The library is open from 9 AM to 5 PM."

Question:
"What are the library timings?"

Expected response:
"9 AM to 5 PM."

Check whether the answer is supported by the supplied context.

### Scenario 4: Hallucination Testing

Ask a question with a known factual answer.

Compare the model's response with a reliable reference
and identify fabricated or incorrect information.

## 11. Key Takeaways

- LLMs generate text using learned patterns.
- Prompts guide model behaviour.
- Tokens are the units processed by the model.
- Context windows limit the information available
  in a single interaction.
- Temperature influences response variation.
- Inference means generating output using a trained model.
- Hallucinations are a major challenge in LLM testing.
- LLM testing evaluates more than exact output matching.
