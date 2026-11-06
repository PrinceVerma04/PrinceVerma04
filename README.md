<!-- ============================== HEADER ============================== -->
<p align="center">
  <img src="assets/hero.svg" alt="Prince Verma: AI/ML Engineer | Computer Vision | OCR | GenAI" width="100%"/>
</p>

<p align="center">
  <a href="https://prince-portfolio.princeiith.workers.dev/">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&width=650&lines=AI%2FML+Engineer+%40+Coral+Innovation;Production+OCR+%7C+304ms+to+20ms+with+INT8;Computer+Vision+%2B+Speech+AI+%2B+RAG;M.Tech+Smart+Mobility+%40+IIT+Hyderabad" alt="Typing tagline"/>
  </a>
</p>

<p align="center">
  <a href="https://prince-portfolio.princeiith.workers.dev/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white" alt="Portfolio"/></a>
  <a href="https://www.linkedin.com/in/princeverma0411/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:tovermaprince@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://youtube.com/@princeiithvlogs"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"/></a>
  <a href="https://instagram.com/ig.prince04"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"/></a>
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"/></p>

## 👨‍💻 About Me

I build ML systems that hold up in production: models that are accurate on messy real-world data, fast on CPU and edge hardware, and wrapped in pipelines people can actually use.

```python
class PrinceVerma:
    role      = "AI/ML Engineer @ Coral Innovation Pvt. Ltd."
    education = ["M.Tech Smart Mobility, IIT Hyderabad (2026)",
                 "B.Tech, BBDNITM Lucknow (2022)"]
    focus     = ["Production OCR & Document AI",
                 "Computer Vision & Edge Deployment",
                 "Speech AI & Audio Deepfake Detection",
                 "RAG Pipelines & LLM Agents"]
    principle = "Ship models that run fast in production, not just in notebooks"
    open_to   = "Collaborations in ML, CV, NLP and Generative AI"
```

<p align="center"><img src="assets/divider.svg" alt="" width="100%"/></p>

## 🚀 Featured Work

### 1. [Meter Serial OCR](https://github.com/PrinceVerma04/meter-serial-ocr): production OCR for utility meters

<a href="https://github.com/PrinceVerma04/meter-serial-ocr"><img src="assets/card-ocr.svg" alt="Meter Serial OCR highlights" width="100%"/></a>

Fine-tuned **PaddleOCR PP-OCRv5** on field photos of meter nameplates and shipped it as a quantized CPU service.

- **83%** exact match on 21K serials the legacy OCR misread, and **93%** on the 18K images human review confirmed readable
- Retrained INT8 model: **99%** on new held-out images (up from 91%) and **91%** on hard human-reviewed images (up from 12%)
- Confidence gate auto-accepts **64%** of reads at **96.8% precision** on a 4.3K blind test, and holds **95.4%** accuracy on an unseen utility with no retraining
- INT8 post-training quantization: **81 MB → 21 MB** and **304 ms → 20 ms** per image on CPU (15× faster), with **98.6%** FP32-to-INT8 agreement after fixing a silent export failure
- Served as an **ONNX Runtime REST API** with Flask, Docker, systemd and health checks

```mermaid
flowchart LR
    A[Meter photo] --> B[PP-OCRv5 INT8<br/>ONNX Runtime]
    B --> C{Confidence gate}
    C -->|high| D[Auto-accept]
    C -->|medium| E[Human review]
    C -->|low| F[Recapture]
```

`PaddleOCR` `ONNX Runtime` `INT8 PTQ` `Flask` `Docker` `systemd`

### 2. [Civic Monitor](https://github.com/PrinceVerma04/Civic-monitor): civic-issue detection on the edge

<a href="https://github.com/PrinceVerma04/Civic-monitor"><img src="assets/card-civic.svg" alt="Civic Monitor highlights" width="100%"/></a>

**YOLOv8m** detector for 10 civic-issue classes, trained on a 17,000+ image real-world dataset.

- **0.80 mAP@50 / 0.70 mAP@50-95** on a long-tailed detection task
- Audited the raw corpus, merged 7 confusable classes and quarantined **~4,500 mislabeled samples**
- Synthetic night / rain / fog augmentation for robustness in poor field conditions
- Compressed to an **INT8 TFLite model (~26 MB)** with NNAPI for real-time, fully offline on-device inference

`YOLOv8` `PyTorch` `TFLite` `NNAPI` `Data QA`

### 3. [NVIDIA NIM RAG Voice Assistant](https://github.com/PrinceVerma04/nvidia-nim-rag-voice-assistant): voice Q&A over PDFs

<a href="https://github.com/PrinceVerma04/nvidia-nim-rag-voice-assistant"><img src="assets/card-rag.svg" alt="NVIDIA NIM RAG Voice Assistant highlights" width="100%"/></a>

- PDF question answering with **NVIDIA NIM** LLMs and grounded, source-linked answers
- **FAISS** retrieval over NVIDIA embeddings
- Voice queries through **NVIDIA Canary ASR**, in a Streamlit chat interface

`NVIDIA NIM` `RAG` `FAISS` `Canary ASR` `Streamlit`

### 4. [Speaker Identification with X-Vectors](https://github.com/PrinceVerma04/Speaker-Identification--X-vector)

<a href="https://github.com/PrinceVerma04/Speaker-Identification--X-vector"><img src="assets/card-xvector.svg" alt="Speaker Identification highlights" width="100%"/></a>

- Deep speaker identification and verification using the **X-Vector** architecture
- **93% accuracy** on multi-speaker datasets

`PyTorch` `X-Vector` `Speaker Recognition`

### 5. [SLIM-XA: Audio Deepfake Detection](https://github.com/PrinceVerma04/SLIM-with-cross-attention) · M.Tech Thesis

<a href="https://github.com/PrinceVerma04/SLIM-with-cross-attention"><img src="assets/card-slim.svg" alt="SLIM-XA highlights" width="100%"/></a>

- Extends **SLIM (NeurIPS 2024)** with bidirectional 4-head cross-attention between Wav2Vec2-XLSR style and linguistic representations
- Two-stage training: real-only, then real/fake classification
- On ASVspoof 2019 LA: **90% accuracy**, **99.98% fake-speech recall**, 22.37% EER on unseen attacks

`Wav2Vec2-XLSR` `Cross-Attention` `ASVspoof`

<p align="center"><img src="assets/divider.svg" alt="" width="100%"/></p>

## 🔬 Research

**WildSpoof Challenge · IEEE ICASSP 2026 Grand Challenge**: participated with a spoofing-aware speaker verification (SASV) system that rejects both wrong speakers and synthetic speech in noisy real-world audio. Worked with SpoofCeleb (2.5M+ utterances, 1,251 speakers, 23 TTS systems).

<p align="center"><img src="assets/divider.svg" alt="" width="100%"/></p>

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| **Languages** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black) ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white) ![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=flat-square) |
| **Deep Learning** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) |
| **Computer Vision & OCR** | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white) ![YOLO](https://img.shields.io/badge/YOLOv8-111F68?style=flat-square) ![PaddleOCR](https://img.shields.io/badge/PaddleOCR-0062B0?style=flat-square) ![Grad-CAM](https://img.shields.io/badge/Grad--CAM-555555?style=flat-square) |
| **Generative AI** | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square) ![NVIDIA NIM](https://img.shields.io/badge/NVIDIA%20NIM-76B900?style=flat-square&logo=nvidia&logoColor=white) ![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square) ![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square) |
| **Deployment & Optimization** | ![ONNX](https://img.shields.io/badge/ONNX%20Runtime-005CED?style=flat-square&logo=onnx&logoColor=white) ![TFLite](https://img.shields.io/badge/TFLite-FF6F00?style=flat-square&logo=tensorflow&logoColor=white) ![INT8](https://img.shields.io/badge/INT8%20Quantization-6A1B9A?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) |
| **Data & Tools** | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white) |

<p align="center"><img src="assets/divider.svg" alt="" width="100%"/></p>

## 🏆 Achievements

- 🥇 **Winner**, AgriTech AI Hackathon 2025 (KIT Skill Hub & Pavaman Technologies)
- 🎯 **GATE 2024**, All India Rank **498**
- 🌏 Selected participant, Global Consumer Intelligence Program, Matsuo Laboratory, The University of Tokyo
- 🥈 2nd Prize, IIC & AICTE Ideation Contest (EV Charging through Smart Grid)

<p align="center"><img src="assets/divider.svg" alt="" width="100%"/></p>

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.shion.dev/api?username=PrinceVerma04&theme=github_dark&hide_border=true&show_icons=true&include_all_commits=false&count_private=false" height="165" alt="GitHub stats"/>
  <img src="https://github-readme-stats.shion.dev/api/top-langs/?username=PrinceVerma04&theme=github_dark&hide_border=true&layout=compact" height="165" alt="Top languages"/>
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=PrinceVerma04&theme=github-dark-blue&hide_border=true" alt="GitHub streak"/>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=PrinceVerma04&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views"/>
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"/></p>

## 🌱 Currently Working On

Personal projects in progress:

- **YouTube Product Review Analysis**: analysing product-review videos and their comments to understand what viewers really think about a product
- **OCR & Local Vision Models in Production**: fine-tuning OCR models and taking local vision models into production

<!-- ============================== FOOTER ============================== -->
<p align="center">
  <img src="assets/footer.svg" alt="" width="100%"/>
</p>
