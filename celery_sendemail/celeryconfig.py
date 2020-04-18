# Celery本身不含消息服务，它使用第三方消息服务来传递任务
# 选redis作为消息服务（Broker），Celery默认使用的是RabbitMQ
# 也可以通过 -b 选项在命令行进行设置其他的中间人（Broker）
broker_url = 'redis://127.0.0.1:6379/1'

# 保存结果：如果想跟踪任务状态，Celery需要存储任务状态信息.
# Celery 内置了一些后端结果：SQLAlchemy/Django ORM、Memcached、Redis、 RPC (RabbitMQ/AMQP)以及自定义的后端结果存储中间件
backend=''

# 指定序列化方式
task_serializer = 'json'

# 指定区时间
tiemzone = 'Asia/Shanghai'

# 导入任务模块列表
include=['celery_test.tasks',]