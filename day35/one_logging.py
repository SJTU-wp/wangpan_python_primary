# author: wp
# 2022年03月26日 16:48
# 使用logging日志框架，理解日志级别，日志需要包含的一些信息

# 日志输出到控制台
import logging
# 日志信息：时间，文件名[位置]，日志级别，信息
# logging.basicConfig(level=logging.WARNING,  # 大于等于这里级别的日志才会输出
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# # 开始使用log功能，传递的参数会替换message
# logging.debug('这是 logging debug message')
# logging.info('这是 logging info message')
# logging.warning('这是 logging a warning message')
# logging.error('这是 an logging error message')
# logging.critical('这是 logging critical message')


# 日志输出到文件
logging.basicConfig(level=logging.INFO,
                    filename='log1.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    encoding='utf8')

logging.debug('这是 logging debug message')
logging.info('这是 logging info message')
logging.warning('这是 logging a warning message')
logging.error('这是 an logging error message')
logging.critical('这是 logging critical message')
