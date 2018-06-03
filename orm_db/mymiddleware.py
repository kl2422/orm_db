from django.utils.deprecation import MiddlewareMixin


class LoggerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("打印request信息。。。。")

    # 获取请求参数以及返回的结果
    def process_response(self, request, response):
        try:
            path = request.path
            method = request.method
            params = None
            if method == 'GET':
                params = request.GET
            else:
                params = request.POST
            if params:
                params_str = str(dict(params))
            meta = request.META
            # 客户端IP地址。
            remote_addr = meta['REMOTE_ADDR']
            # REMOTE_HOST ：客户端主机名。
            remote_host = meta['REMOTE_HOST']
            # HTTP_HOST ：客户端发送请求HOST。
            http_host = meta['HTTP_HOST']
            # 客户端的user - agent字符串。
            user_agent = meta['HTTP_USER_AGENT']

            print("""
                            请求路径[{path}],
                            请求方法[{method}],
                            请求参数[{params}],
                            客户端IP地址[{remote_addr}],
                            客户端主机名[{remote_host}],
                            客户端发送请求主机[{http_host}],
                            客户端的user_agent[{user_agent}]
                            """.format(path=path, method=method, params=params_str,
                                       remote_addr=remote_addr, remote_host=remote_host,
                                       http_host=http_host, user_agent=user_agent))

            if response.streaming:
                print("响应的content:", str(response.streaming_content, encoding='utf-8'))
            else:
                print("响应的content:", str(response.content, encoding='utf-8'))

        except Exception:
            pass

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("处理视图模板")
        print(view_func)
        print(view_args)
        print(view_kwargs)

    # def process_template_response(self, request, response):
    #     print("响应模板视图。。。")

    def process_exception(self, request, exception):
        print("视图异常类。。。")


