import random
from scrapy.exceptions import NotConfigured


class RandomProxyMiddleware(object):

    def __init__(self, settings):
        self.proxies = settings.getlist('PROXIES')
        if not self.proxies:
            raise NotConfigured
        self.stats = {}.fromkeys(self.proxies, 0)
        # for proxy in self.proxies:
        #     self.stats[proxy] = 0
        self.max_failed = 1

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        return cls(crawler.settings)

    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(self.proxies)
        print('++++++++++++++++++++use %s as proxy' % request.meta['proxy'])

    def process_response(self, request, response, spider):

        # 判断代理池中的正在使用的IP是否可用
        cur_proxy = request.meta['proxy']

        if response.status >= 400:
            self.stats[cur_proxy] += 1

        if self.stats[cur_proxy] >= self.max_failed:
            self.remove_proxy(cur_proxy)

        if response.status < 400:
            return response

        del request.meta['proxy']
        return request

    # 进程异常
    def process_exception(self, request, exception, spider):
        cur_proxy = request.meta['proxy']
        # 打印引发的异常
        print('raise exception: %s when use %s ' % (exception, cur_proxy))
        self.remove_proxy(cur_proxy)
        del request.meta['proxy']
        return request

    def remove_proxy(self, proxy):
        if proxy in self.proxies:
            self.proxies.remove(proxy)
            print('============proxy %s removed from proxies list' % proxy)





























