import grpc
import services_pb2
import services_pb2_grpc
from concurrent import futures
import time
from sentiment_analysis_service import SentimentAnalysisService

class TextInputService(services_pb2_grpc.TextInputServiceServicer):
    def __init__(self, sentiment_service):
        self.sentiment_service = sentiment_service

    def ProcessText(self, request, context):
        text = request.text
        sentiment_result = self.sentiment_service.sentiment_analysis(text)
        return services_pb2.SentimentResponse(sentiment=sentiment_result)

def serve(sentiment_service):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_TextInputServiceServicer_to_server(TextInputService(sentiment_service), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    # Assuming SentimentAnalysisService is defined and working correctly
    sentiment_service = SentimentAnalysisService()
    serve(sentiment_service)
