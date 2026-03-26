# Spam Email Detection System 


##  Overview of the Project
This project implements a simple spam email detection system using core Python concepts. The system analyzes the text of an email and classifies it as either Spam or Ham (Not Spam).

The project is designed to demonstrate how basic machine learning logic, inspired by the Naive Bayes approach, can be implemented without using external libraries. It focuses on simplicity, clarity, and understanding of fundamental concepts.

---

##  Features
- Accepts email text input from user  
- Preprocesses text (lowercase, punctuation removal)  
- Classifies emails as spam or not spam  
- Uses word frequency-based logic  
- Lightweight and fast execution  
- No external dependencies required  
- Easy to understand and modify  

---

##  Technologies / Tools Used
- Python (Built-in libraries only)  
- String handling  
- Lists and Dictionaries (for data storage)  

---

##  Steps to Install & Run the Project

1. Install Python (if not already installed)  
2. Copy the project code into a file named:
   spam_detector.py  
3. Open terminal or command prompt  
4. Run the following command:

   python spam_detector.py  

---

##  Instructions for Testing
1. Run the program  
2. Enter any email text when prompted  
3. Observe the output classification  
4. Try different inputs such as spam-like and normal messages  
5. Type 'exit' to stop the program  

---

## Problem Statement
Spam emails are unwanted messages that can be misleading or harmful. The problem is to design a system that can automatically detect whether an email is spam or not based on its content.

---

##  Objectives
- To develop a basic spam detection system  
- To understand text preprocessing techniques  
- To implement classification logic manually  
- To avoid dependency on external libraries  
- To demonstrate modular programming  

---

##  Functional Requirements
- Accept email input from user  
- Clean and preprocess text  
- Store and analyze word frequencies  
- Train a simple model using sample data  
- Predict spam or ham classification  
- Display result clearly  
- Allow repeated user interaction  

---

##  Non-Functional Requirements
- **Performance:** Fast execution  
- **Security:** No external data usage  
- **Usability:** Simple interface  
- **Reliability:** Consistent results  
- **Scalability:** Can be extended with more data  
- **Maintainability:** Modular code structure  
- **Resource Efficiency:** Minimal memory usage  

---

## System Architecture Diagram
User → Input Module → Preprocessing → Model Logic → Prediction → Output  
![WhatsApp Image 2026-03-26 at 10 05 54 PM](https://github.com/user-attachments/assets/cdd01a2c-ffae-4b11-be4c-ddfb56954dd2)

---

##  Process Flow / Workflow Diagram
![WhatsApp Image 2026-03-26 at 10 08 08 PM](https://github.com/user-attachments/assets/08cdb757-6f35-4681-9765-82dd608c4fce)


##  UML Diagrams

### 🔹 Use Case Diagram
User → Enter Email  
System → Process Email  
System → Predict Spam/Ham  
System → Display Result  

---

### 🔹 Class / Component Diagram
Class: SpamDetector  

Functions:  
- load_data()  
- preprocess()  
- train_model()  
- predict()  
- run_system()  

---![WhatsApp Image 2026-03-26 at 10 09 58 PM](https://github.com/user-attachments/assets/09b4e3d9-bd2e-4a6d-a046-d3617beed48f)


### 🔹 Sequence Diagram
User → System: Enter Email  
System → Preprocessing: Clean Text  
Preprocessing → Model: Process Data  
Model → System: Return Prediction  
System → User: Display Result  

---

##  Database / Storage Design

### 🔹 ER Diagram
Emails → List  
Labels → List  
SpamWords → Dictionary  
HamWords → Dictionary  

---

### 🔹 Schema Design
Emails: List of email strings  
Labels: List of classifications (spam/ham)  
SpamWords: Dictionary storing word frequency  
HamWords: Dictionary storing word frequency  

---

##  Dataset Description
The dataset used is a small, manually created dataset containing sample spam and non-spam emails.

Example:
- "Win money now" → Spam  
- "Let's meet tomorrow" → Ham  

This dataset is used for demonstration purposes only.

---

##  Model Selection Rationale
A Naive Bayes-inspired approach is used because:
- It is simple and easy to implement  
- Works well for text classification problems  
- Does not require complex computations  
- Suitable for beginner-level understanding  

---

## Evaluation Methodology
- Manual testing with different inputs  
- Checking correctness of predictions  
- Comparing spam and ham scores  
- Observing consistency in results  

---

##  Conclusion
This project demonstrates how spam detection can be implemented using basic Python programming. It helps in understanding the fundamentals of text processing and classification without relying on advanced libraries.

---
