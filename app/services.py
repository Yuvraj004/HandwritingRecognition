from sklearn.datasets import load_digits

from app.classifier import ClassifierFactory
from app.image_processing import process_image 

class PredictDigitService:
    def __init__(self, repo):
        self.repo = repo

    def handle(self, image_data_uri):
        classifier = self.repo.get()
        if classifier is None:
            digits = load_digits()
            classifier = ClassifierFactory.create_with_fit(
                digits.data, # type: ignore
                digits.target # type: ignore
            )
            self.repo.update(classifier)
        
        x = process_image(image_data_uri)
        if x is None:
            return 0

        prediction = classifier.predict(x)[0] # type: ignore
        return prediction
    
