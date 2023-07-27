# text_input_service.py
import grpc
import services_pb2
import services_pb2_grpc
from concurrent import futures
import time

class TextInputService(services_pb2_grpc.TextInputServiceServicer):
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.sentiment_stub = services_pb2_grpc.SentimentAnalysisServiceStub(self.channel)

    def ProcessText(self, request, context):
        text = request.text

        # 将文本数据发送到情感分析服务进行处理
        sentiment_result = self.send_request_to_sentiment_service(text)

        return services_pb2.SentimentResponse(sentiment=sentiment_result)

    def send_request_to_sentiment_service(self, text):
        request = services_pb2.TextRequest(text=text)
        response = self.sentiment_stub.AnalyzeSentiment(request)
        return response.sentiment

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_TextInputServiceServicer_to_server(TextInputService(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
