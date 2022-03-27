# author: wp
# 2022年03月26日 20:17
# 日志既输出到文件，也输出到屏幕

import logging

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # log等级总开关

# 第二步，创建一个handler，用于写入日志文件
fh = logging.FileHandler('log2.txt', 'a', encoding='utf8')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到console的log等级开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，把fh和ch添加到logger中
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')
