# 🎨 Heritatech Solutions (ArtRestorer AI)
## CRS Artificial Intelligence – Generative AI Summative Assessment

---

## 👤 Student Details

- **Student Name:** Nishtha Priyesh Shah  
- **Candidate Registration Number:** 1000436  
- **CRS Name:** Artificial Intelligence  
- **Course Name:** Generative AI  
- **School Name:** Aspee Nutan Academy  
- **Live Link:** *https://htwsk6nb6ezpiwfwl45n8u.streamlit.app/*

---

## 🌍 Project Overview

### 📌 Scenario Selected  
**Scenario 1 – Smart Assistance Web Application to Support Art Restoration**

**Heritatech Solutions (ArtRestorer AI)** is a generative AI-powered web application designed to assist:

- Museum Curators  
- Art Historians  
- Conservation Specialists  
- Cultural Researchers  
- Students  

The application uses the **Google Gemini API** to generate:
- Historically accurate insights  
- Culturally sensitive interpretations  
- Professionally structured restoration guidance  

It bridges the gap between:
- **Artificial Intelligence**
- **Cultural Heritage Preservation**

---

## 🧠 Problem Definition & Research

### 🎯 Problem Statement

Across the world, invaluable artworks are deteriorating due to:

- Aging and environmental exposure  
- Fading pigments and discoloration  
- Structural cracks and surface erosion  
- Moisture, mold, and pollution  
- Loss of historical documentation  

Traditional restoration methods require highly specialized expertise, which is often:
- Expensive  
- Time-consuming  
- Geographically limited  

---

## 💡 Proposed Solution

Develop a **Smart Generative AI Assistant** that:

- Accepts artwork metadata (type, period, artist, damage description)  
- Optionally analyzes uploaded artwork images  
- Generates restoration strategies and techniques  
- Provides cultural and historical interpretations  
- Produces visitor-friendly summaries  
- Collects feedback on AI output quality  
- Tracks usage data for analytical insights  

---

## 🤖 Model Integration

### Model Used
python
model = genai.GenerativeModel("gemini-3-flash-preview")
# 🔧 Hyperparameter Tuning

| Parameter | Purpose | Value Used |
|----------|---------|------------|
| temperature | Controls creativity | 0.1 – 1.0 |
| max_output_tokens | Response length | 2048 |

### 🛠 Tuning Strategy

- **Low temperature (0.1–0.3):**  
  Produces historically conservative, factual, and safe restoration outputs.

- **Medium temperature (0.5–0.7):**  
  Balances historical accuracy with creative interpretation.

- **High temperature (0.8–1.0):**  
  Enables creative reconstruction and interpretative analysis while maintaining ethical boundaries.

### 🎨 Art Styles Tested

- Renaissance  
- Mughal  
- Gothic  
- Abstract Expressionism  

---

# 🧩 Prompt Engineering

The system dynamically constructs **structured prompts** using the following parameters:

- Artwork Type  
- Art Period / Style  
- Artist *(optional)*  
- Damage Description  
- Desired Output Format  

This structured approach ensures:

- Reduced hallucinations  
- Improved contextual relevance  
- High cultural and historical sensitivity  

---

## 📌 Core Prompts Implemented

1. Baroque painting missing corner restoration  
2. Mughal miniature floral detailing enhancement  
3. Sandstone sculpture facial reconstruction  
4. 18th-century silk tapestry embroidery repair  
5. Abstract Expressionist texture recreation  
6. Medieval manuscript ink restoration  
7. Mayan glyph carving reconstruction  
8. Ajanta cave mural pigment revival  
9. Japanese Ukiyo-e woodblock enhancement  
10. Gothic cathedral mosaic crack repair  

All prompts are designed to maintain ethical standards and historically grounded restoration practices.

---

# 📤 Output Types

Users can select from the following output formats:

- 🛠 **Restoration Technique**  
- 📖 **Narrative Reconstruction**  
- 🔍 **Symbol Interpretation**  
- 📑 **Complete Professional Analysis**  

Each output is:

- Clearly structured  
- Suitable for academic and museum documentation  
- Easy to interpret for educational audiences  

---

# 📊 Advanced Features

## ⭐ Feedback System

- Cultural accuracy evaluation  
- Technical usefulness assessment  
- Historical alignment rating  
- Clarity and realism scoring  
- Automated quality score generation  

## 📈 Usage Tracking

- User session data logging  
- Timestamped interactions  
- Tabular usage summaries for analysis  

---

# 🧪 Model Validation & Optimization

### 🔍 Tested On

- Oil paintings  
- Sculptures  
- Manuscripts  
- Murals  
- Textiles  
- Pottery and mosaics  

### ✅ Validation Strategy

- Cross-checked outputs with trusted art history references  
- Ensured culturally respectful and non-invasive language  
- Refined prompts based on feedback and accuracy reviews  

---

# 🖥 Web Application Design

## Built Using

- `streamlit`  
- `google-generativeai`  
- `pandas`  
- `datetime`  
- HTML & CSS *(custom UI styling)*  

---

## 🎨 Key UI Features

- Animated splash screen  
- Historic-themed visual design  
- Curator profile creation  
- Multi-tab dashboard  
- Image upload and preview  
- Feedback evaluation interface  
- Clean museum-style yellow theme  

---

# 🚀 Deployment

## Files Included

- `app.py`  
- `requirements.txt`  
- `README.md`  

## Deployment Steps

1. Push the project to a GitHub repository  
2. Deploy the application using **Streamlit Cloud**  
3. Configure the Gemini API key using Streamlit Secrets  
4. Test application functionality across multiple devices  

---

# 📂 Repository Checklist

- [x] Fully functional Streamlit application  
- [x] Gemini API successfully integrated  
- [x] 10+ structured prompts implemented  
- [x] Hyperparameter tuning completed  
- [x] Feedback evaluation system implemented  
- [x] Clean and professional UI/UX  
- [x] README documentation complete  
- [x] Deployed Streamlit web application  

---

# 🎯 Rubric Alignment (Distinction Level)

### 🧠 Problem Understanding & Solution Design  
✔ Addresses a real-world cultural preservation challenge  
✔ Aligns AI usage with ethical and social good  

### 🧩 Prompt Engineering & Creativity  
✔ Context-aware and structured prompt design  
✔ Coverage across multiple art forms and historical periods  

### 📤 Output Quality & Relevance  
✔ Historically grounded outputs  
✔ Culturally sensitive and context-aware responses  

### 🧪 Model Testing & Optimization  
✔ Effective parameter tuning  
✔ Prompt refinement through testing  
✔ Validation across diverse artwork types  

### 🖥 Deployment & Usability  
✔ Fully deployed Streamlit application  
✔ Professional, intuitive interface  
✔ Interactive and user-friendly experience  

---

# 🌟 Conclusion

**Heritatech Solutions (ArtRestorer AI)** demonstrates how Generative AI can:

- Support global cultural preservation efforts  
- Assist art restoration research and planning  
- Democratize access to expert-level art insights  
- Enhance museum, academic, and educational workflows  

The project successfully integrates:

> Advanced AI technology  
> Cultural responsibility  
> Creative problem-solving  
> Real-world application design  

---

## 📌 End of README
