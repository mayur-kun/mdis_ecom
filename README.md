This repository showcases my master's research project focusing on customer churn prediction. Leveraging the power of Google Cloud Platform (GCP), I developed a comprehensive solution to identify customers at risk of attrition and build and automate the CI/CD pipeline.

🌟 Key Highlights:
1. Data Analysis: Utilized BigQuery to analyze large-scale customer data, uncovering patterns and trends influencing churn behavior.
2. Model Development: Built a high-accuracy Random Forest model on Vertex AI to predict customer churn probability.
3. Scalable Deployment: Deployed the model as a Streamlit app for user-friendly insights and predictions, enabling easy integration with existing workflows.
4. GCP Advantages: Demonstrated the benefits of GCP for machine learning projects, including scalability, security, flexibility, and cost-effectiveness.

This project contributes to:
1. Improved customer retention through accurate churn prediction and targeted engagement.
2. Data-driven decision making for businesses based on actionable insights.
3. Showcasing the capabilities of GCP for real-world machine learning applications.

🚀 Explore the repository:
Code for data analysis and model building - model_training.ipynb
Code for frontend - app.py
Deployment specifications for GCP - cloudbuild.yaml
Deployment specifications for local - Dockerfile


🛠️ Steps and Tools:
Here's an overview of the steps involved and the GCP services utilized:

1. Data Preparation:

BigQuery: Used to store and query customer data for analysis.

Cloud Storage: Used for storing the dataset, and the ML models that will be created. Create separate storage buckets for storing data and ML models.

Dataflow (Optional): If complex data transformations are needed, this can be used for data cleaning, pre-processing, and feature engineering.

2. 🧑‍🚒️ Model Building & Training:

Vertex AI: Used for EDA and training various classification models. I have selected the Random Forest model in this case as it gave the best performance. You can also link it with your GitHub repo to make it easy to maintain and update the code.

Cloud Storage: Store the model artifacts after training.

3. 🍽 Deployment & Serving:

Streamlit: Developed a user interface using Streamlit to interact with the model on my local machine.

Cloud Source Repository: Connect this service with your GitHub repo, where all the files () have been pushed. The advantage here is that every time a change is made to any of the files and pushed to the repository, this service will automatically fetch those changes and trigger Cloud Run. Cloud Run will then create a new docker image and deploy the application automatically.

Cloud Run: Deployed the application for real-time prediction access. Cloud Run generates a custom-link that can be accessed by anyone across the web. The generated link remains the same throughout the life-cycle of the project. 
(P.S. I have currently disabled the app link to my project to save my free credits 😝 Feel free to DM or leave a comment for access.)

Artifact Registry: Stored the containerized image, which has all the requirements needed to build and serve the application.

4. ⚙️ Evaluation & Monitoring:

Vertex AI Endpoints (Optional): Used for monitoring model performance and receiving predictions.

5. 💲 Pricing and APIs:

You'll need to enable all the APIs needed for this project through the "APIs and Services" section in the GCP console.

If you are new to GCP, you can use the free credits provided by the platform as I have done for this project. Once the free credits run out, the platform will charge you monthly for the services and compute resources used in your project.


Conclusion:

This project was a fantastic learning experience! I got to dive into the world of GCP and gain practical skills in deploying models and even automating the CI/CD pipeline (which was a big goal for me!). By leveraging BigQuery, Vertex AI, and Streamlit, I built a customer churn prediction model that not only provided valuable insights but also showcased the potential of GCP for real-world data science applications.

I encourage you to browse the code and leave feedback or questions regarding the project :)