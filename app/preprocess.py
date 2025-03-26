import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(input_file, output_file):

    data = pd.read_excel(input_file, engine='openpyxl')
    
 
    encoders = {}
    for column in ["Lead_Actor", "Director", "Keyword_1", "Keyword_2", "Keyword_3"]:
        encoder = LabelEncoder()
        data[column] = encoder.fit_transform(data[column])
        encoders[column] = encoder
    

    genre_encoder = LabelEncoder()
    data["Genre"] = genre_encoder.fit_transform(data["Genre"])
    encoders["Genre"] = genre_encoder
    

    import pickle
    with open("encoders.pkl", "wb") as f:
        pickle.dump(encoders, f)

    data.drop(columns=["Movie_Title"], inplace=True)
    

    data.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Preprocessed data saved to {output_file}")

# Example usage
input_file = "dataset.xlsx"  
output_file = "preprocessed_dataset.xlsx" 
preprocess_data(input_file, output_file)
