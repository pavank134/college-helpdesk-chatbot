import json
import re
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="College Helpdesk Chatbot", page_icon="🎓", layout="centered")
DATA_PATH = Path(__file__).parent / "knowledge_base.json"

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def retrieve(query, documents, top_k=3):
    q_tokens = tokenize(query)
    ranked = []
    for doc in documents:
        d_tokens = tokenize(doc["topic"] + " " + doc["content"] + " " + " ".join(doc["keywords"]))
        score = len(q_tokens & d_tokens) / max(1, len(q_tokens))
        ranked.append((score, doc))
    return sorted(ranked, key=lambda x: x[0], reverse=True)[:top_k]

def answer_for(results, threshold=0.12):
    best_score, best_doc = results[0]
    if best_score < threshold:
        return "I could not find a reliable match in the loaded college information. Please check the latest official notice or contact the relevant college office. I will not guess policy details.", []
    return ("The relevant topic was found, but the approved answer has not been added yet. "
            "Please check the latest official college notice or contact the relevant office. "
            "This chatbot will not invent attendance rules, exam dates, lab timings, or event details."), [best_doc]

with open(DATA_PATH, "r", encoding="utf-8") as f:
    knowledge = json.load(f)

st.title("🎓 College Helpdesk Chatbot")
st.caption("A retrieval-first prototype for attendance, examinations, labs, and events.")
st.warning("DEMO ONLY: This knowledge base contains placeholders, not your college's official rules. Do not rely on it for deadlines or policy decisions.")
with st.expander("How does it work?"):
    st.markdown("1. Student enters a question.\\n2. The app searches a local knowledge base.\\n3. It displays a matching source entry.\\n4. If evidence is missing or weak, it abstains and directs the student to an official channel.\\n\\nThis is a retrieval-first teaching prototype, not a full generative RAG system. It does not call an LLM or use embeddings.")

examples = [
    "What is the minimum attendance required?",
    "Where can I find the semester exam timetable?",
    "When is the computer lab record submission?",
    "What is the date of the college fest?",
    "How can I ask about an attendance shortage?"
]
choice = st.selectbox("Try a sample question or choose custom", ["Type my own question"] + examples)
question = st.text_input("Your question", value="" if choice == "Type my own question" else choice)
if st.button("Search approved information", type="primary") and question.strip():
    results = retrieve(question, knowledge)
    response, docs = answer_for(results)
    st.subheader("Chatbot response")
    st.write(response)
    st.subheader("Retrieval evidence")
    if docs:
        for doc in docs:
            st.markdown(f"**Source ID:** `{doc['source_id']}`")
            st.markdown(f"**Topic:** {doc['topic']}")
            st.write(doc["content"])
            st.caption("Source status: PLACEHOLDER — replace with an approved document")
    else:
        st.write("No sufficiently relevant source was found.")
    with st.expander("Debug: top retrieval matches"):
        for score, doc in results:
            st.write(f"{score:.2f} — {doc['source_id']} — {doc['topic']}")

st.divider()
st.subheader("Knowledge-base readiness")
st.metric("Topics loaded", len(knowledge))
st.metric("Entries awaiting official content", sum(1 for d in knowledge if d.get("placeholder", False)))
st.caption("Before deployment, college staff must approve documents, maintain current versions, test citations, and define escalation contacts. Avoid collecting student IDs, grades, phone numbers, or other personal data in this demo.")
