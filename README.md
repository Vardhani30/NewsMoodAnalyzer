# **NewsMoodAnalyzer**

## **Project Overview**

**NewsMoodAnalyzer** is a sentiment analysis project designed to analyze the sentiment of news articles. The project uses Python, Flask, and various natural language processing (NLP) libraries to scrape news data, analyze sentiment, and present the results in a web-based interface. The analysis is focused on articles sourced from Blackoffer news, and results are displayed using interactive visualizations.

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Input and Output Files](#input-and-output-files)
8. [Acknowledgments](#acknowledgments)

## **Features**

- Web scraping to collect news articles from various sources.
- Sentiment analysis of news articles using NLP techniques.
- Interactive web interface to display sentiment analysis results.
- Capability to handle input and output through Excel files.
- Modular code structure for easy maintenance and extension.


## **Requirements**

To run this project, you'll need the following software and libraries:

- **Python** (version 3.6+)
- **Pandas** (data manipulation)
- **Openpyxl** (Excel file handling)
- **BeautifulSoup** (web scraping)
- **Requests** (HTTP requests)
- **xlrd** (optional, but note its limitation on `.xlsx` files)
- **TextBlob** (NLP for sentiment analysis)

## **Installation**

Follow these steps to set up and run the project:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/sentiment_analysis_project.git
   cd sentiment_analysis_project
