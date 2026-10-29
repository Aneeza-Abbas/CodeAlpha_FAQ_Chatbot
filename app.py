
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# FAQ knowledge base
faqs = [
    {
        "keywords": ["artificial intelligence", "what is ai", "define ai"],
        "answer": "Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that normally require human intelligence."
    },
    {
        "keywords": ["machine learning", "what is ml"],
        "answer": "Machine Learning (ML) is a branch of AI that allows computers to learn patterns from data and make predictions."
    },
    {
        "keywords": ["python", "programming language"],
        "answer": "Python is a beginner-friendly programming language used in web development, automation, data science, and artificial intelligence."
    },
    {
        "keywords": ["chatbot", "what is a bot"],
        "answer": "A chatbot is a computer program that communicates with users through text or speech and answers their questions."
    },
    {
        "keywords": ["deep learning"],
        "answer": "Deep Learning is a type of machine learning that uses multi-layered neural networks to learn complex patterns from data."
    },
    {
        "keywords": ["natural language processing", "what is nlp", "nlp"],
        "answer": "Natural Language Processing (NLP) is a branch of AI that helps computers understand, interpret, and generate human language."
    },
    {
        "keywords": ["neural network", "neural networks"],
        "answer": "A neural network is a computing model inspired by the human brain. It learns patterns from data using interconnected artificial neurons."
    },
    {
        "keywords": ["data science", "what is data science"],
        "answer": "Data science combines statistics, programming, and data analysis to discover useful information and patterns from data."
    },
    {
        "keywords": ["supervised learning"],
        "answer": "Supervised learning is a machine learning approach in which a model learns from labeled training examples."
    },
    {
        "keywords": ["unsupervised learning"],
        "answer": "Unsupervised learning is a machine learning approach that finds patterns or groups in data without labeled answers."
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip().lower()

    if not question:
        return jsonify({
            "answer": "Please enter a question."
        })

    # Match the question against the FAQ knowledge base
    for faq in faqs:
        if any(keyword in question for keyword in faq["keywords"]):
            return jsonify({
                "answer": faq["answer"]
            })

    # Fallback response for unknown questions
    return jsonify({
        "answer": (
            "Sorry, I don't know that answer yet. "
            "Please try asking about AI, machine learning, Python, "
            "chatbots, deep learning, NLP, neural networks, "
            "data science, supervised learning, or unsupervised learning."
        )
    })


if __name__ == "__main__":
    app.run(debug=True)
