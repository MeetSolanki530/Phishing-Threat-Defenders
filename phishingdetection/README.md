# Project Name: Create an intelligent system using AI/ML to detect phishing domains which imitate look and feel of genuine domains
# PS Code : 1454

## Team Name: Phishing Threat Defenders
- Team Members: 
- Ravi Solanki
- Manav Patel
- Shani Darji
- Meet Solanki
- Vrunda Bhuva
- Shreya Shah

## Contact Email: 
-solankiravi2674@gmail.com
-manavp571@gmail.com
-darji.shani8155@gmail.com
-solankimeet530@gmail.com

## Project Overview 🚀
-We are currently working on a project where we are building an intelligent system using AI and ML to identify phishing domains. These are fake websites that try to look like real ones to trick people into giving away their information. Using the skills we've been learning in machine learning, we are creating a program that can automatically spot these deceptive websites by analyzing their appearance and other features. As we continue to develop this project, we are also planning to add the ability to analyze images for an even more robust detection system.

## Tech Stack 💻

Here are the technologies and tools we used to build our AI solution:

-Machine Learning: Python, Scikit Learn
-Natural Language Processing: NLTK
-Data Pre-processing: Pandas, NumPy, Seaborn, Matplotlib
-Web Development: Flask, HTML, Python
-Image Analysis: Deep Learning 
-Chatbot: Azure Cognitive Services
-Model Deployment: AWS/Azure

## Project Features and Functionality ✨

-Phishing Domain Identification: The core functionality of our AI project is its ability to automatically identify phishing domains. It analyzes various aspects of a website, such as its URL structure, content, and visual elements, to determine if it's likely a phishing site.

-Real-time Detection: Users will benefit from real-time detection capabilities. When they visit a website, our AI system can quickly assess whether it's a potential phishing domain or not. This real-time analysis adds a layer of security to their online activities.

-Scalability: The AI system is designed to handle a large number of websites, making it suitable for both individual users and organizations. It can efficiently process and evaluate numerous websites concurrently.

- User Interaction:

  -Website Analysis: Users can interact with the system by simply inputting a website URL. The AI will quickly analyze the site and provide a report on whether it's       safe or potentially a phishing domain.

  -Feedback Submission: If a user disagrees with the system's assessment, they can provide feedback, helping to refine the AI model's accuracy.

  -Settings Configuration: Users have the flexibility to customize the system's behavior, allowing them to tailor the level of protection according to their needs.

## How It Works 🛠️
![phishing%20workflow.png](attachment:phishing%20workflow.png)

Provide a high-level overview of how our AI solution works. You can use diagrams or flowcharts to make it easier to understand. Explain the key components, data flow, and the AI/ML techniques utilized.

The Phishing Domain Detection system utilizes artificial intelligence and machine learning to identify and block phishing domains in real-time. It processes website URLs through tokenization and stemming, converts them into numerical features, and employs machine learning models such as Logistic Regression and Multinomial Naive Bayes for classification. Users interact with the system through a user-friendly interface, inputting URLs for analysis, and can provide feedback to enhance accuracy. This system enhances online security by swiftly identifying potential phishing websites, offering real-time protection, and allowing customization to meet individual security preferences, ultimately providing a safer online experience for users.

#### Data Flow:

    -Data Input: The dataset containing URLs and labels is loaded into the program.
    -Preprocessing: The URLs undergo tokenization, stemming, and text concatenation to prepare them for feature extraction.
    -Feature Extraction: CountVectorizer converts the text data into numerical features.
    -Data Splitting: The dataset is split into training and testing sets.
    -Model Training: Logistic Regression and Multinomial Naive Bayes models are trained on the training data.
    -Model Evaluation: The models are evaluated using the testing data, and various metrics are calculated to assess their performance.
    -Best Model Selection: Logistic Regression is identified as the best-performing model.
    -Model Deployment: The Logistic Regression model is deployed using a pipeline and saved for future use.

#### AI/ML Techniques Utilized:

    -Tokenization: To break down URLs into individual words or tokens.
    -Stemming: To reduce words to their root forms, aiding in text analysis.
    -CountVectorizer: To convert text data into numerical features for machine learning.
    -Logistic Regression: A machine learning algorithm for binary classification tasks.
    -Multinomial Naive Bayes: Another classification algorithm suitable for text-based data.
    -Train-Test Split: To divide the dataset into training and testing subsets for model evaluation.
    -Model Evaluation Metrics: Classification reports, confusion matrices, and accuracy are used to evaluate model performance.

## Challenges and Solutions 🧠
Share any challenges our team faced during development and how you overcame them. This can include technical obstacles, data-related issues, or creative roadblocks.

#### Challenges Faced:

During the development of our Phishing Domain Detection system, our team encountered a notable challenge. This challenge was specifically related to how our model handled URLs with the "https://" prefix. These URLs, commonly used for secure web communication, were causing our model to predict inaccurate results. This issue posed a significant obstacle to the system's effectiveness, as it needed to perform reliably regardless of the URL format it encountered.

#### The Solution Implemented:

To address this challenge, we devised a solution within our Flask application. We recognized that the issue stemmed from the format disparity between the URLs and our model's expectations. To mitigate this, we introduced a crucial preprocessing step. This step involved automatically removing the "http://" part from URLs before sending them for analysis by our model. By implementing this condition, we ensured that the URLs were consistently formatted to match our model's training data. This adjustment significantly improved the accuracy and reliability of our Phishing Domain Detection system.

## Future Enhancements 🚧

Chat Bot Using Azure Cognitive Services: Another exciting addition we are planning is the integration of a chatbot into our project, powered by Azure Cognitive Services. This chatbot will serve as a helpful assistant for users, capable of answering questions and providing valuable information regarding phishing sites. It will make our project more interactive and user-friendly, offering a seamless experience for anyone who uses it.

## Screenshots and Demos 📸
Showcase the visual aspects of our AI solution through screenshots or videos. If possible, include a link to a live demo or video demonstration.
![Screenshot%20%28183%29.png](attachment:Screenshot%20%28183%29.png)

![Screenshot%20%28184%29.png](attachment:Screenshot%20%28184%29.png)

![Screenshot%20%28185%29.png](attachment:Screenshot%20%28185%29.png)

## Acknowledgments 🙌


## Get In Touch! 📬


| Team Member | LinkedIn | Kaggle | Email |
|---|---|---|---|
| Manav Patel | [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/manav-patel-571-aiml/) | [![Kaggle](https://img.shields.io/badge/Kaggle-%2320B2AA.svg?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/manavpatel571) | [manavp571@gmai.com](mailto:manavp571@gmail.com) |
| Shani Darji | [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/shani-darji-59b2a8263) | [![Kaggle](https://img.shields.io/badge/Kaggle-%2320B2AA.svg?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/shanidarji) | [darji.shani8155@gmail.com](mailto:darji.shani8155@gmail.com) |
| Ravi Solanki | [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/solankiravi2674/) | [![Kaggle](https://img.shields.io/badge/Kaggle-%2320B2AA.svg?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/solankiravi2674) | [ravi260720041@outlook.com](mailto:ravi260720041@outlook.com) |
| Meet Solanki | [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/meet-solanki-000245292) | [![Kaggle](https://img.shields.io/badge/Kaggle-%2320B2AA.svg?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/meetsolanki530) | [solankimeet530@gmail.com](mailto:solankimeet530@gmail.com) |
| Vrunda Bhuva | [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/vrunda-bhuva-b0b2a626b) | [![Kaggle](https://img.shields.io/badge/Kaggle-%2320B2AA.svg?style=for-the-badge&logo=kaggle)]() | [vrundabhuva8@gmail.com](mailto:vrundabhuva8@gmail.com) |




---

