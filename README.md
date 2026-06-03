# Multi-Factor Student Verification System

A Python-based student authentication system that combines barcode scanning and facial recognition for secure identity verification.

## Overview

This project was developed as a first-semester ICT project to demonstrate the practical application of computer vision and biometric authentication.

The system uses a two-step verification process:

1. The student's CMS ID is scanned through a barcode.
2. The student's face is verified against a registered facial database.

Access is granted only when both verifications are successful.

---

## Features

* Real-time barcode scanning
* CMS ID validation using an Excel database
* Facial recognition authentication
* Multi-factor verification workflow
* Face database management
* Verification timeout handling
* Access granted / denied feedback
* Live webcam processing

---

## System Workflow

```text
Scan Barcode
      ↓
Is CMS ID Valid?
      ↓
      Yes
      ↓
Show Face to Camera
      ↓
Face Match Found?
      ↓
 ┌───────────┴───────────┐
 │                       │
Yes                     No
 │                       │
 ↓                       ↓
Access Granted     Access Denied
```

## Technologies Used

* Python
* OpenCV
* Pyzbar
* Face Recognition
* OpenPyXL
* NumPy
* Webcam Video Processing

---

## Project Structure

```text
project/
│
├── faces/
│   ├── 101.jpg
│   ├── 102.jpg
│   ├── ...
│
├── students.xlsx
├── main.py
├── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/student-verification-system.git
cd student-verification-system
```

### Install Dependencies

```bash
pip install opencv-python
pip install pyzbar
pip install face-recognition
pip install openpyxl
```

Or install everything using:

```bash
pip install -r requirements.txt
```

---

## Configuration

### Student Database

Create an Excel file named:

```text
students.xlsx
```

Column A should contain valid CMS IDs.

Example:

| CMS ID |
| ------ |
| 101    |
| 102    |
| 103    |

### Face Database

Create a folder named:

```text
faces
```

Store student images inside the folder.

The filename must match the student's CMS ID.

Example:

```text
faces/
├── 101.jpg
├── 102.jpg
├── 103.jpg
```

---

## How It Works

### Stage 1: Barcode Verification

The system continuously scans incoming frames from the webcam.

When a barcode is detected:

* The CMS ID is extracted.
* The ID is checked against the Excel database.
* If valid, the system enters face verification mode.

### Stage 2: Face Verification

The user has 10 seconds to present their face.

The system:

* Detects the face from the live webcam feed.
* Generates a facial encoding.
* Retrieves the stored encoding associated with the scanned CMS ID.
* Compares both encodings.

If the match is successful:

```text
ACCESS GRANTED
```

Otherwise:

```text
FACE MISMATCH
```

or

```text
FACE NOT REGISTERED
```

---

## Learning Outcomes

This project helped me gain hands-on experience with:

* Computer Vision
* Facial Recognition Systems
* Biometric Authentication
* State-Based Program Design
* Real-Time Video Processing
* Python Libraries and API Integration
* Software Engineering Fundamentals

---

## Future Improvements

* Database integration (MySQL/PostgreSQL)
* Attendance logging system
* Admin dashboard
* QR code support
* Multi-face detection
* Anti-spoofing protection
* Cloud-based student records

---

## Author

Ali Bin Naseer
