import grpc
import services_pb2
import services_pb2_grpc
from concurrent import futures
import time
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

class SentimentAnalysisService(services_pb2_grpc.SentimentAnalysisServiceServicer):
    def __init__(self):
        self.model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")
        self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def AnalyzeSentiment(self, request, context):
        text = request.text
        sentiment_result = self.sentiment_analysis(text)
        return services_pb2.SentimentResponse(sentiment=sentiment_result)

    def sentiment_analysis(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        inputs.to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=1)
            sentiment_label = torch.argmax(probabilities, dim=1)
            sentiments = ['negative', 'positive']
            return sentiments[sentiment_label]

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_SentimentAnalysisServiceServicer_to_server(SentimentAnalysisService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
