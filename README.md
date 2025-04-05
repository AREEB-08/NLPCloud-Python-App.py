# 🌟 NLPCloud-Python-App.py

🚀 An interactive Python NLP application powered by NLP Cloud API, packed with powerful NLP features and a user-friendly experience.

---

## 🔥 Overview
This Python-based NLP application includes:

- ✅ Named Entity Recognition (NER)
- ✅ Language Detection
- ✅ Sentiment Analysis
- ✅ English-to-Hindi Translation
- ✅ AI-Powered Code Generation

🔐 It also includes:
- User Authentication (Register/Login)
- Easy-to-navigate menu system

---

## 🛠️ Installation Guide

### 📌 Prerequisites
Make sure you have Python **3.8 or above** installed.
```bash
python --version
```

### 📦 Install Required Packages
```bash
pip install nlpcloud tabulate
```

### 🔑 Get Your NLP Cloud API Key
1. Go to 👉 [https://nlpcloud.com](https://nlpcloud.com)
2. Sign up / Login
3. Copy your **API Key** from the dashboard
4. Replace `"YOUR_API_KEY_HERE"` in the code with your key:
```python
client = nlpcloud.Client("finetuned-llama-3-70b", "YOUR_API_KEY_HERE", gpu=True)
```

---

## 🚀 How to Run

### 📥 Clone and Run in One Click:
Click the button below to download the repo directly:

[![Download ZIP](https://img.shields.io/badge/⬇️%20Download%20Repository-NLPCloud--Python--App.py-green)](https://github.com/AREEB-08/NLPCloud-Python-App.py/archive/refs/heads/main.zip)

Then run:
```bash
cd NLPCloud-Python-App.py
python your_script.py
```

---

## 🎯 Features & Usage

### 🔍 1. Named Entity Recognition (NER)
Extracts key entities like **names, organizations, dates** from your text.
```bash
Enter the text: Elon Musk founded Tesla in 2003.
Enter the target category: Person
```
📌 Output: `Elon Musk (Person)`

### 🌍 2. Language Detection
Detects the language of any input text.
```bash
Enter text: Bonjour tout le monde!
```
📌 Output: `French (Probability: 0.98)`

### 😊 3. Sentiment Analysis
Identifies if the statement is **Positive**, **Negative**, or **Neutral**.
```bash
Enter text: I love this product!
```
📌 Output: `Positive (Score: 0.95)`

### 🇮🇳 4. English → Hindi Translation
Translate any English sentence into Hindi.
```bash
Enter text: Hello, how are you?
```
📌 Output: `नमस्ते, आप कैसे हैं?`

### 💻 5. AI-Powered Code Generation
Turn natural language prompts into real code.
```bash
Enter language: Python
Enter instruction: Generate a Python script to sort a list of numbers.
```
📌 Output: Python script code

---

## ⚠️ Notes
- 💡 Replace the **API Key** in the code before running
- 🔒 **Never share your API Key** publicly
- ⚙️ Ensure all dependencies are installed
- 🧾 Inputs like **email during login are case-sensitive**

---

## 🖥️ Screenshots / Demo
*(Optional: Add screenshots showing login, menu, and output)*

---

## 🏆 Contributor
Developed with ❤️ by [AREEB-08](https://github.com/AREEB-08)

If you like this project, **⭐ star it on GitHub!**

---

## 📌 Suggested Repository Name:
**NLPCloud-Python-App.py** ✅

Enjoy exploring NLP like never before! 🚀✨

