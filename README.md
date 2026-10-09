# College Helpdesk Chatbot — Problem 7

## Important
This retrieval-first prototype uses placeholder knowledge-base entries because no actual college regulations or notices were provided. It intentionally does not invent attendance percentages, exam dates, lab timings, or event details.

It is not a full generative RAG system: it uses simple keyword overlap, returns a matching source entry, and abstains when evidence is missing. It does not call an LLM or use embeddings.

## Run
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. `python -m pip install -r requirements.txt`
4. `python -m streamlit run app.py`
5. Open the local URL shown in the terminal, usually http://localhost:8501.

## Demo
Try questions about attendance, exam timetables, lab submissions, college events, and helpdesk contact. The app should state that official information is not loaded and direct the student to an official channel.

## Production RAG workflow
Collect approved official documents; record owner/version/effective date; split documents into chunks; index them using embeddings and/or keyword search; retrieve relevant passages; generate answers only from those passages; cite document title/page/date; abstain on missing or conflicting evidence; escalate sensitive cases; enforce access controls and data retention.

## Official tool links
- Streamlit chat interface: https://docs.streamlit.io/develop/api-reference/chat
- OpenAI File Search: https://developers.openai.com/api/docs/guides/tools-file-search
- OpenAI Retrieval: https://developers.openai.com/api/docs/guides/retrieval
- LangChain learning docs: https://docs.langchain.com/oss/python/learn
