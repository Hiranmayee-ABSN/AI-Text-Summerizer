
# AI Text Summerizer
A simple and elegant web app built using **Streamlit** that allows users to:
- Summarize long articles or paragraphs using a **pre-trained Transformer model**
- Optionally translate the summary to a different language (e.g., Telugu, Hindi, French)

---

## Features

✅ Paste any article or paragraph  
✅ Generate a short, readable summary using **Hugging Face Transformers**  
✅ Translate the summary using **Deep Translator**  
✅ Lightweight, runs entirely in your browser via **Streamlit**

---

##  Built With

- [Streamlit](https://streamlit.io/) – For the interactive UI
- [Transformers (Hugging Face)](https://huggingface.co/transformers/) – For text summarization (`distilbart-cnn-12-6`)
- [Deep-Translator](https://pypi.org/project/deep-translator/) – For language translation

## Installation

### Step 1: Clone the project

```bash
git clone https://github.com/yourusername/ai-text-summarizer.git
cd ai-text-summarizer
````

### Step 2: Install dependencies

```bash
pip install streamlit transformers sentencepiece deep-translator
```
## Run the App

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```
##Supported Translation Languages
You can enter a **language code** like:
| Language | Code |
| -------- | ---- |
| Telugu   | `te` |
| Hindi    | `hi` |
| French   | `fr` |
| Tamil    | `ta` |
| Spanish  | `es` |
Full list: [Deep Translator Language List](https://pypi.org/project/deep-translator/)
## 💡 Example Use Case
Paste this into the app:
```
Reading has long been considered one of the most transformative habits a person can cultivate...
```
Click **"Summarize"** → View the summary → Optionally translate it.
## License
MIT License. Use it freely, improve it, or contribute back!
