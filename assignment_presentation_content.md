# Problem 7 — College Helpdesk Chatbot

## 1. Domain and Target User
**Domain:** Customer service / education technology.  
**Target users:** Students who ask about attendance, examinations, labs, college events, and helpdesk procedures. College staff approve and maintain the information.

## 2. Problem Statement
Students repeatedly ask the same questions about attendance, exams, labs, and events. Answers may be delayed or inconsistent when information is spread across notices, PDFs, websites, and department offices. The chatbot should retrieve answers from approved college information and direct students to staff when evidence is missing.

## 3. Required Task and Expected Output
Build a chatbot prototype/design that uses approved college information. Deliver a prototype, five sample questions, a discussion of RAG, and evaluation of grounded accuracy, citations, escalation, and privacy.

## 4. AI Tools Used and Official Links
- **Streamlit:** chat interface and prototype — https://docs.streamlit.io/develop/api-reference/chat
- **OpenAI File Search / Retrieval (optional production component):** search approved files — https://developers.openai.com/api/docs/guides/tools-file-search and https://developers.openai.com/api/docs/guides/retrieval
- **LangChain (optional):** RAG and semantic retrieval workflows — https://docs.langchain.com/oss/python/learn
- **Python:** application logic.

**Prototype honesty:** The supplied demo is retrieval-first and uses keyword overlap. It is not a full LLM-based RAG system. Since no actual college policy documents were provided, its knowledge base contains placeholders and it refuses to invent official facts.

## 5. Prompts Used and Short Output Examples
**Prompt for a future LLM-based RAG system:**  
“You are the college helpdesk assistant. Answer only using retrieved approved college passages. Cite source title and page or notice date. If information is missing, conflicting, or outdated, say you cannot verify it and direct the student to the relevant office. Never invent attendance rules, exam dates, lab deadlines, event details, or contact information. Do not request sensitive personal data in chat.”

**Q1: What is the minimum attendance required?**  
Output: “The approved attendance policy is not loaded in this demo, so I cannot verify the required percentage. Please check current academic regulations or contact your department office.” Source: `ATT-PLACEHOLDER-01` (not official).

**Q2: Where can I find the semester exam timetable?**  
Output: “The current examination notice is not loaded. Please check the official examination-cell notice. I cannot confirm dates from this demo.” Source: `EXAM-PLACEHOLDER-01`.

**Q3: When is the computer lab record submission?**  
Output: “The approved lab schedule is not loaded. Please ask your lab faculty or department office; this demo will not guess a deadline.” Source: `LAB-PLACEHOLDER-01`.

**Q4: What is the date of the college fest?**  
Output: “The current event circular is not loaded. Please check official college announcements for the date and registration details.” Source: `EVENT-PLACEHOLDER-01`.

**Q5: How can I ask about an attendance shortage?**  
Output: “Please contact your department office or the official college helpdesk. Verified contact details must be added before this chatbot can provide a phone number or email.” Source: `HELP-PLACEHOLDER-01`.

## 6. Evaluation Criteria and Observations
| Criterion | How to evaluate | Expected observation |
|---|---|---|
| Grounded accuracy | Check answers against official source | No invented policy details |
| Citation quality | Verify source title, page, version, date | Citation supports the answer |
| Retrieval relevance | Test direct and paraphrased questions | Correct notice ranks highly |
| Abstention | Ask questions absent from knowledge base | Bot says it cannot verify |
| Escalation | Ask personal, urgent, disputed, or unclear questions | Route to staff |
| Privacy | Check data stored | Collect only necessary data |
| Freshness | Check old notices | Superseded notices are marked or removed |

The keyword-based prototype demonstrates retrieval and abstention but may miss synonyms. It must be tested with paraphrased questions and approved documents before deployment.

## 7. Limitations, Risks, and Human Checks
- Old notices may give incorrect dates. Store version and effective date.
- Generative models can hallucinate. Restrict answers to retrieved evidence and require citations.
- Keyword retrieval may miss synonyms; production can combine embeddings and keyword search.
- Conflicting documents must be escalated.
- Avoid collecting student IDs, marks, credentials, health details, or personal case histories unless an approved process requires them.
- Separate public FAQs from private student records and apply access controls.
- Staff must approve documents, monitor unanswered questions, review errors, and maintain updates.

## 8. Final Recommendation with Justification
Build a Streamlit prototype connected to a curated, approved college knowledge base. For production, use RAG to retrieve relevant passages, generate answers strictly from those passages, and cite sources. If evidence is missing or uncertain, the chatbot should abstain and route the student to the relevant office. This prioritizes accuracy, transparency, privacy, and human oversight.

## RAG in simple words
**RAG = Retrieval + Augmented + Generation.**
1. Retrieval: search official college documents.
2. Augmented: provide the retrieved passages to a language model as context.
3. Generation: write a simple answer based on those passages and cite them.

RAG can reduce unsupported answers, but it does not guarantee correctness. Source quality, retrieval quality, citations, and human review still matter.

## References
- Streamlit chat interface: https://docs.streamlit.io/develop/api-reference/chat
- OpenAI File Search: https://developers.openai.com/api/docs/guides/tools-file-search
- OpenAI Retrieval: https://developers.openai.com/api/docs/guides/retrieval
- LangChain documentation: https://docs.langchain.com/oss/python/learn
