from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import joblib
import numpy as np

# Load the trained KNN model and encoders
knn_model = joblib.load('./app/knn_model.pkl')
encoders = joblib.load('./app/encoders.pkl')

def input_page(request):
    return render(request, 'input.html')

def predict_genre(request):
    if request.method == "POST":
        # Get user input
        lead_actor = request.POST.get('lead_actor')
        director = request.POST.get('director')
        keyword_1 = request.POST.get('keyword_1')
        keyword_2 = request.POST.get('keyword_2')
        keyword_3 = request.POST.get('keyword_3')

        # Encode user input using saved encoders
        try:
            encoded_input = [
                encoders['Lead_Actor'].transform([lead_actor])[0],
                encoders['Director'].transform([director])[0],
                encoders['Keyword_1'].transform([keyword_1])[0],
                encoders['Keyword_2'].transform([keyword_2])[0],
                encoders['Keyword_3'].transform([keyword_3])[0],
            ]
        except ValueError:
            return JsonResponse({'error': 'Invalid input. Please check the values.'}, status=400)

        # Reshape input for prediction
        encoded_input = np.array(encoded_input).reshape(1, -1)

        # Predict genre
        predicted_genre = knn_model.predict(encoded_input)
        genre = encoders['Genre'].inverse_transform(predicted_genre)[0]

        # Return the result
        return JsonResponse({'predicted_genre': genre})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
