<!-- PROJECT LOGO -->
<br />
<div align="center">
   <p align="center">
     <img src="https://github.com/Pupuk-In/.github/assets/87064650/2db0c8de-65c6-4f6e-81ba-645db1219d31" alt="pupukin-logo" width="400px">
   </p>
  <h3 align="center">Pupuk.In</h3>
  <p align="center">
    The machine learning side of Pupuk.In application.
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
The Pupuk.In application utilizes three machine learning models. Each model is developed with the aim of assisting users in selecting and conducting transactions smoothly. The three models are as follows:

1. Nutrient Deficiency Symptoms Detection
This model classifies plants that have nutrient deficiencies. Currently, the model is capable of classifying input images of rice plants into three classes: Nitrogen, Potassium, and Phosphorus.
2. Product Search Relevance
This model takes a search query as input and sorts the available products based on their relevance to the search query.
3. Product Recommendation
This model calculates recommendations for each user based on their unique purchase history to provide suitable product recommendations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DATASETS -->
## Datasets
1. Nutrient Deficiency Symptoms in Rice: https://www.kaggle.com/datasets/guy007/nutrientdeficiencysymptomsinrice

This dataset used to train the Nutrient Deficiency Detection model. This dataset consists only images of rice leaf. In the future, its best to add more plant types datasets.
### Sample
![image](https://github.com/Pupuk-In/Machine-Learning/assets/62583810/d3e98fa7-964c-4d28-bffc-1437b442901a)

2. Machine Translated Indonesian STS-B: https://huggingface.co/datasets/LazarusNLP/stsb_mt_id

This dataset used to train a NLU model to calculate the similarity of sentences by comparing the text embeddings with cosine similarity.
### Sample
![image](https://github.com/Pupuk-In/Machine-Learning/assets/62583810/581d4752-e4ae-4ef5-a6f5-90ede7576215)

3. Pupuk.In syntesis product: https://github.com/Pupuk-In/product-recommendation/blob/main/Dataset%20Produk%20Pupuk.csv

This dataset used to test the product recommendation model output.
### Sample
![image](https://github.com/Pupuk-In/Machine-Learning/assets/62583810/42c093b6-0fba-4435-a799-a20b44e9aa8e)
