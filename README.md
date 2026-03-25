# 🧠  Optical Character Recognition on Android using Google ML Kit

<p align="center">
  <img src="https://github.com/Lettie-a-code/CSE-5120_Homework_2_codes_files/blob/main/AndriodPhone.png" width="50%">
</p>

---

## Home Page

---

Welcome to Optical Character Recognition **(OCR)** home page!

---

# 🧠Introduction
This application was developed as part of a Software Engineering course **(CSE 4500)** under Dr. Jennifer Jin at California State University, San Bernardino. The project was a team-based effort to develop a bill-splitting mobile application. 

---
 
##  💡Overview
**This project demonstrates:**

1. On-device OCR using Google ML Kit
2. Camera integration using CameraX
3. Real-time mobile image capture
4. Structured Android architecture
---

### Why Use Google ML Kit for OCR?

- 🔍 ML Kit **abstracts** the complexities of machine learning, allowing developers to build rich user experiences with ready-to-use APIs.

- ⏰ Most ML kit processing occurs on the device.  Offering **real-time** performance due to zero network latency,

- 🎯 Google ML kit offers a variety of pre-trained models for common mobile use cases in **vision** and **natural language** processing.

---

<table style="width: 100%;">
<tr>
<td style="vertical-align: top; text-align: left; width: 50%; font-size: 18px;">

### The OCR pipeline consists of the following stages:

1. 💻 Camera initialization

2. 🖥️ Image capture  

3. 🔧 InputImage Conversion

4. 🛠️ Text Processing

5. 🖥️ Display Results

</td>
<td style="text-align: center; width: 50%; font-size: 18px;">

### OCR Implementation Milestones

<img src="https://github.com/Lettie-a-code/CSE-5120_Homework_2_codes_files/blob/main/OCR_implementationSteps.png" alt="OCR implementation steps" width="400">

</td>
</tr>
</table>

---

# 📘 Progress
---

## 🎤 Results

---
### 📌App Installed on Android Device
The application was successfully deployed and installed on a physical Android device.
<p align="center">
   <img src="https://github.com/Lettie-a-code/CSE-5120_Homework_2_codes_files/blob/main/images/appInstalled_on_Android.png" width="40%">
</p>


---
### 📌 OCR Output on Device
The system successfully detects and displays text captured from the camera input. For example, the phrase "HELLO WORLD" was partiallyy recognized and rendered in the application interface

<p align="center">
  <img src="https://github.com/Lettie-a-code/CSE-5120_Homework_2_codes_files/blob/main/images/imageCaptured.png" width="40%">
</p>

---

### 📌Logcat Output Showing OCR Result

Logcat output confirms that the OCR process executes correctly, with recognized text being processed through the ML Kit pipeline.

<p align="center">
  <img src="https://github.com/Lettie-a-code/CSE-5120_Homework_2_codes_files/blob/main/images/LogCat_view.png" width="60%">
</p>
 
---

# 🛠️ Key Engineering Challenges encountered so far

- Gradle wrapper incompatibility
  
- JVM target mismatch
  
- AppCompat theme conflict

# 🎤 What is next for the OCR application?

- Conduct quality assurance testing for improved character and digit recognition accuracy

-  Evaluate performance under varying lighting and image conditions
The Android Studio project for the OCR component is maintained in a separate repository due to its size, platform-specific dependencies, and independent development lifecycle.

This repository includes only the core backend and supporting documentation. The Android mobile application can be accessed at the following location:

**Android OCR Repository:**  
👉 https://github.com/Lettie-a-code/projectOCR_v2

# ❓ Why a Separate Repository?

The Android Studio project is managed independently to:
- Maintain clear separation of platform-specific code
- Simplify dependency management and build configurations
- Support independent development, testing, and deployment cycles
- Improve repository performance and maintainability

Please refer to the Android repository for installation instructions, build steps, and mobile-specific documentation.

-  Enhance UI/UX for better user interaction
