# -*- coding: utf-8 -*-

# Scrapy settings for xpc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xpc'

SPIDER_MODULES = ['xpc.spiders']
NEWSPIDER_MODULE = 'xpc.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agenter
#USER_AGENT = 'xpc (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

CONCURRENT_REQUESTS = 4

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# REDIS_URL = 'redis:user:pass@hostname:6379'
REDIS_URL = 'redis:127.0.0.1:6379'
SCHEDULER_PERSIST = True

ITEM_PIPELINES = {
   'xpc.pipelines.MysqlPipeline': 300,
   # 'scrapy_redis.pipelines.RedisPipeline': 301,
}



DOWNLOAD_TIMEOUT = 10

HTTPPROXY_ENABLED = True
PROXIES = [
   'http://47.100.176.209:1703',
]

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
   'Accept-encoding': "gzip, deflate",
   'Accept-language': "zh-CN,zh;q=0.9,fr;q=0.8",
   'Connection': "keep-alive",
   'Cookie': "Device_ID=5b0b75b236c83; Authorization=14E50ADCBB41420ABBB4144F90BB414B5D1BB414CC8321F6CB31; _ga=GA1.2.620218388.1527477684; zg_did=%7B%22did%22%3A%20%22163a4c3c9e8185-055a4121da6e08-336b7b05-13c680-163a4c3c9e9a1%22%7D; UM_distinctid=163a4c3d2b251-047a3999538a02-336b7b05-13c680-163a4c3d2b3911; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22163a4c40e1c4c0-01bc440ddcaaf6-336b7b05-1296000-163a4c40e1daa7%22%2C%22%24device_id%22%3A%22163a4c40e1c4c0-01bc440ddcaaf6-336b7b05-1296000-163a4c40e1daa7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gid=GA1.2.1595248466.1527730627; ts_uptime=0; CNZZDATA1262268826=2146381837-1527477522-%7C1527729099; PHPSESSID=6t85htiekgtofs1rbrs4h985p0; Hm_lvt_dfbb354a7c147964edec94b42797c7ac=1527563680,1527564024,1527730632,1527733730; _gat=1; zg_c9c6d79f996741ee958c338e28f881d0=%7B%22sid%22%3A%201527733524.313%2C%22updated%22%3A%201527733827.562%2C%22info%22%3A%201527477684722%2C%22cuid%22%3A%2010345094%7D; Hm_lpvt_dfbb354a7c147964edec94b42797c7ac=1527733828; responseTimeline=195; cn_1262268826_dplus=%7B%22distinct_id%22%3A%20%22163a4c3d2b251-047a3999538a02-336b7b05-13c680-163a4c3d2b3911%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201527733833%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201527733833%7D%7D",
   'Host': "www.xinpianchang.com",
   'Upgrade-insecure-requests': "1",
   'User-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
   'Cache-control': "no-cache",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xpc.middlewares.XpcSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
   'xpc.middlewares.RandomProxyMiddleware': 543,
}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
