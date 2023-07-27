# grpc_client.py
import grpc
import services_pb2
import services_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50050')
    stub = services_pb2_grpc.TextInputServiceStub(channel)

    while True:
        text = input("请输入文本（输入'exit'退出测试）：")
        if text.lower() == 'exit':
            break

        request = services_pb2.TextRequest(text=text)
        response = stub.ProcessText(request)
        print("情感极性：", response.sentiment)

if __name__ == '__main__':
    run()
