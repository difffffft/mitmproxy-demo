from mitmproxy import ctx, http, websocket


class Counter:

    def __init__(self):
        pass

    def request(self, flow: http.HTTPFlow):
        print(flow.request.url)
        pass

    def response(self, flow: http.HTTPFlow):
        print(flow.request.url)


addons = [
    Counter()
]
