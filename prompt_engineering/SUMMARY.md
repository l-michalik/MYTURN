# Prompt Engineering Techniques

This document explains the most efficient prompt engineering methods.  
Each section includes a short description and minimal example.  
At the end, you’ll find a **summary table** showing when to use each method.  

---

## 1. Basic Prompting (Task / Context / Reference / Format)

### Description
The foundation of effective prompting. Always define what you want, give background, show examples, and specify format.  

### Example
- **Task:** "Summarize this report."  
- **Context:** "It’s for a business meeting with non-technical managers."  
- **Reference:** "Follow the style of last week’s summary."  
- **Format:** "Write in 5 bullet points, each under 12 words."  

---

## 2. Multimodal Prompting

### Description
Combine text with images, charts, or audio. Give the AI clear instructions on what to do with multimodal inputs.  

### Example
- *Prompt:* "Describe the key trend in this chart in 3 bullet points."  
- *Context:* "The description will be used in a budget report for executives."  
- *Format:* "Each bullet point should be under 10 words."  

---

## 3. Prompt Chaining

### Description
Break a complex task into smaller, connected steps. Each output becomes the input for the next step.  

### Example
1. *Step 1:* "List 5 reasons why sales dropped in Q3."  
2. *Step 2:* "For each reason, suggest a solution."  
3. *Step 3:* "Summarize the solutions into a 1-page report."  

---

## 4. Chain of Thought

### Description
Encourage the AI to reason step by step before giving the final answer.  

### Example
- *Prompt:* "Solve: A train goes 60 km/h for 2h, then 90 km/h for 3h. What is the total distance? Think step by step."  
- *AI thinking:* "60×2 = 120. 90×3 = 270. 120+270=390."  
- *Answer:* "The total distance is 390 km."  

---

## 5. Few-Shot Prompting

### Description
Provide examples in your prompt to guide style, tone, or structure.  

### Example
- *Prompt:*  
  ```
  Example 1: Question: What is AI?  
  Answer: AI is the ability of machines to mimic human intelligence.  

  Example 2: Question: What is ML?  
  Answer: ML is a subset of AI focused on learning from data.  

  Now: Question: What is Deep Learning?  
  Answer:
  ```  

---

## 6. Role Prompting

### Description
Ask the AI to take on a role or persona to improve relevance and style.  

### Example
- *Prompt:* "You are a career coach. Suggest 3 interview tips for a software engineer applying at a startup."  

---

## 7. Constraints Prompting

### Description
Set boundaries for the answer (word limits, tone, style, structure).  

### Example
- *Prompt:* "Summarize this article in exactly 3 bullet points, each under 8 words, no jargon."  

---

## 8. Self-Critique (Reflexion)

### Description
Ask the AI to review and improve its own answer.  

### Example
1. *Step 1:* "Summarize this article in 3 sentences."  
2. *Step 2:* "Now check if the summary is clear and non-technical. Improve it if necessary."  

---

# Summary of Methods

| Technique             | Best For                                               |
|-----------------------|--------------------------------------------------------|
| **Basic Prompting**   | Everyday use, clear communication                      |
| **Multimodal**        | Tasks with images, charts, or audio                    |
| **Prompt Chaining**   | Multi-step workflows and structured tasks              |
| **Chain of Thought**  | Logic, reasoning, math, problem-solving                |
| **Few-Shot**          | Mimicking style, tone, or specific output structure    |
| **Role Prompting**    | Simulations, expertise, tailored advice                |
| **Constraints**       | Focused, concise outputs with strict requirements      |
| **Self-Critique**     | Quality improvement, refining unclear answers          |

---

## Which One Is Best When?

- Use **Basic Prompting** as the default foundation.  
- Add **Multimodal** when working with images, charts, or audio.  
- Use **Prompt Chaining** for big workflows that need step-by-step structure.  
- Use **Chain of Thought** for logic-heavy or math problems.  
- Use **Few-Shot** when you want the output to match a style or format.  
- Use **Role Prompting** when simulating an expert or persona helps.  
- Add **Constraints** to keep the AI focused and concise.  
- Add **Self-Critique** if you want the AI to refine and improve its own answer.  