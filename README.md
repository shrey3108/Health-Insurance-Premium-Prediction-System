# Health-Insurance-Premium-Prediction-System

Health Insurance Premium Prediction System

# Introduction
In today’s fast-paced world, health insurance has become a vital necessity. With rising medical costs and unpredictable lifestyles, people are increasingly opting for insurance coverage. However, determining the right insurance premium for each individual is often a complex task involving various personal and health-related parameters. Traditional methods used by insurance companies rely heavily on manual evaluation and predefined slabs, which may not reflect actual risk or affordability. This project aims to leverage machine learning techniques to develop a system that can accurately predict health insurance premiums based on user inputs. By analyzing data patterns, the system can offer precise, customized premium predictions that are both reliable and efficient.
# Project Overview
The objective of this project is to build a machine learning model that predicts the annual health insurance premium of an individual using relevant features like age, income, region, insurance plan, lifestyle habits, and health status. The system uses regression algorithms to learn patterns from historical data and produce accurate predictions. A total of 17 input features are taken from users, processed, and passed to a trained machine learning model. Among the three models tested—Linear Regression, Ridge Regression, and XGBoost—the XGBoost model provided the best performance. The final model is deployed with a user-friendly interface using Streamlit, allowing real-time predictions based on user input.
# Dataset and Preprocessing
The dataset for this project was collected from Kaggle and contains approximately 50,000 rows with detailed records of individuals, including demographic and health-related attributes along with their annual insurance premiums. Data preprocessing involved transforming categorical variables into numerical values using one-hot encoding and mapping techniques. For example, gender, region, marital status, BMI category, smoking status, and employment type were converted to binary or ordinal values. To ensure uniformity in model training, all features were normalized using Min-Max Scaling. This ensured that every feature had equal importance during training. The final dataset consisted of 17 numerical input features used across all models.
# Feature Engineering
To prepare the dataset for machine learning modeling, extensive feature engineering was performed. The original dataset contained 17 relevant attributes that encompassed demographic, health, lifestyle, and financial information. Several categorical variables were converted into numerical format to make them compatible with regression algorithms. For example, gender was encoded as binary values where Male was represented as 1 and Female as 0. Similarly, marital status was encoded as 1 for Unmarried and 0 for Married, while insurance plans were treated as ordinal values—Bronze as 0, Silver as 1, and Gold as 2.
One-hot encoding was applied to non-ordinal categorical variables such as region, BMI category, smoking status, and employment status. In the case of region, Northeast was used as the base category, and the remaining three (Northwest, Southeast, and Southwest) were converted into separate binary columns. After encoding, the final structure included 3 columns for region, 3 for BMI category, 2 for smoking status, 2 for employment status, and one each for gender, marital status, and insurance plan.
To ensure uniform contribution of all features, numerical values were scaled using Min-Max normalization. This transformation brought all values into the range of 0 to 1, which is especially important for algorithms like linear and ridge regression. After all transformations, the final input feature vector consisted of 17 well-processed columns, which were then used for model training and evaluation.
# Model Building and Evaluation
Three regression models were trained and tested—Linear Regression, Ridge Regression, and XGBoost. Both Linear and Ridge Regression models achieved an R² score of 0.92, indicating a good fit. However, the XGBoost model significantly outperformed them with an R² score of 0.97. The XGBoost model's high accuracy is due to its gradient boosting architecture, which allows it to model complex non-linear relationships efficiently. This model was saved using Pickle for deployment purposes. Each model was evaluated based on its prediction accuracy, generalization ability, and consistency across varied data conditions. The XGBoost model was chosen for final deployment due to its superior performance.


 
# Results and Business Use Case
The system demonstrated high accuracy, with XGBoost achieving an R² score of 0.97. From a business perspective, this model holds significant value for insurance providers. It can be used to streamline the premium calculation process, offer personalized pricing, reduce human intervention, and improve customer satisfaction. Users can understand how their personal and lifestyle attributes influence premiums, promoting transparency and better health choices.
Key Factors Affecting Your Premium
Several key factors influence the premium amount an individual has to pay. These include:
•	Age and number of dependents
•	Insurance plan type
•	BMI category and smoking status
•	Employment status and income
These factors are incorporated into the system, allowing users to see the financial implications of their lifestyle and health decisions.
Conclusion and Future Work
The Health Insurance Premium Prediction System effectively showcases how machine learning can be applied to real-world financial services. By using advanced regression techniques and well-structured feature engineering, the system achieves high prediction accuracy. In future, the model can be improved by integrating medical history, claim records, and family health background. Additionally, linking the model with live insurance APIs could enable users to compare premiums and policies in real-time.
The model is also deployment-ready and can be integrated into lightweight web frameworks like Streamlet to provide real-time predictions through a user interface. Furthermore, insurance providers can adopt this tool to offer more personalized and data-driven services to their customers.

