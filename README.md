# Emotitunes

Emotitunes is an innovative web application that merges advanced technologies to create an emotionally responsive music recommendation platform. By analyzing users' facial expressions in real-time, Emotitunes curates personalized music playlists to enhance their emotional experience.

---

## Introduction

In today’s digital age, personalized and emotionally adaptive systems enhance user engagement and experience. Emotitunes leverages cloud computing, AI, and facial recognition technologies to provide mood-based music recommendations in real-time.

---

## Features

1. **Real-time Emotion Detection**:
   - Analyzes facial expressions using TensorFlow and OpenCV.
   - Detects emotional states like happiness, sadness, or neutrality.

2. **Personalized Music Recommendations**:
   - Provides curated playlists that align with users' emotional states.

3. **Scalable Cloud Infrastructure**:
   - Uses AWS services like EC2, RDS, S3, and Cognito for hosting, database management, and secure authentication.

4. **Secure User Authentication**:
   - Supports seamless login and signup via AWS Cognito, including single sign-on with Google.

5. **Media Management**:
   - Efficiently stores and retrieves static files like songs and album images from AWS S3.

---

## Technologies Used

- **Frameworks**: Django (Web Framework)
- **Machine Learning**: TensorFlow, OpenCV
- **Cloud Services**:
  - AWS EC2 (Compute)
  - AWS S3 (Storage)
  - AWS RDS (Database)
  - AWS Cognito (Authentication)
- **Frontend**: HTML, CSS

---

## System Architecture

The application is built on a cloud-based architecture to ensure scalability, reliability, and efficient resource utilization. Key components include:

1. **Emotion Detection**: Facial expressions are analyzed using machine learning models in TensorFlow integrated with OpenCV.
2. **Cloud Services**:
   - EC2 for scalable hosting.
   - S3 for media file management.
   - RDS for secure data storage.
   - Cognito for secure and seamless user authentication.
3. **Dynamic Music Recommendation**: Matches detected moods with relevant playlists.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/emotitunes.git
   cd emotitunes

---

## Results
The application successfully detects user moods (happy, sad, neutral) and provides relevant music recommendations. The scalable cloud infrastructure ensures reliability and responsiveness even under high user demand.

---

## Future Enhancements
1. Support for additional emotional states and more diverse playlists.
2. Integration with other music platforms like Spotify or Apple Music.
3. Mobile app development for on-the-go access.
4. Advanced facial recognition for multi-user support.

---
## Contributors
* Crystal Fernandes (9539)
* Sanika Patankar (9563)
