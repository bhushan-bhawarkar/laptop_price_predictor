# Laptop Price Predictor

Welcome to the Laptop Price Predictor project! This project aims to predict the prices of laptops by scraping data from Amazon and utilizing several machine learning algorithms. After experimenting with various algorithms, the random forest algorithm yielded the best results for predicting laptop prices accurately.

## Dataset

The dataset used for training and testing the laptop price predictor model was obtained by scraping laptop listings from Amazon. The dataset contains the following features:

- Brand: The brand of the laptop.
- Processor: The processor type and model.
- RAM: The amount of RAM in the laptop.
- Storage: The storage capacity of the laptop.
- Display Size: The size of the laptop's display.
- Graphics Card: The graphics card details, if applicable.
- Operating System: The operating system installed on the laptop.
- Price: The price of the laptop (target variable).

## Algorithms Used

Multiple machine learning algorithms were implemented to predict laptop prices. However, after thorough experimentation, the random forest algorithm demonstrated the best performance. It provided accurate predictions by considering the interactions among different features and handling non-linear relationships effectively.

## Usage

To use the laptop price predictor, follow these steps:

1. Install the required dependencies specified in the `requirements.txt` file.
2. Run the data scraping script to collect the latest laptop data from Amazon.
3. Preprocess the dataset by cleaning the data, handling missing values, and encoding categorical variables if necessary.
4. Split the dataset into training and testing sets.
5. Train the random forest model on the training set.
6. Evaluate the model's performance on the testing set using appropriate metrics, such as mean absolute error (MAE) or root mean squared error (RMSE).
7. Once the model is trained, you can use it to predict the prices of new laptops by providing their features as input.

## File Structure

The project follows the following file structure:


## Future Improvements

Here are a few potential areas for future improvement and enhancement:

- Incorporating additional features: Explore the possibility of including more features, such as customer reviews or ratings, to improve the prediction accuracy.
- Hyperparameter tuning: Experiment with different hyperparameter settings for the random forest algorithm to further optimize its performance.
- Web application: Develop a user-friendly web application where users can input laptop specifications and obtain predicted prices instantly.


## Contact

If you have any questions or feedback, feel free to reach out to us at [bhushanbhawarkar32@gmailcom].

Happy predicting!

[Bhushan Bhawarkar]
