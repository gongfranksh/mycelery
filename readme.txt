#启动 worker
#分别在三个终端窗口启动三个队列的worker，执行命令如下所示：
celery -A myCeleryProj.app worker -Q default -l info
celery -A myCeleryProj.app worker -Q tasks_A -l info
celery -A myCeleryProj.app worker -Q tasks_B -l info
#当然也可以一次启动多个队列，如下则表示一次启动两个队列tasks_A，tasks_B。
celery -A myCeleryProj.app worker -Q tasks_A,tasks_B -l info
#则表示一次启动两个队列tasks_A，tasks_B。
#最后我们再开启一个窗口来调用task: 注意观察worker界面的输出
>>> from myCeleryProj.tasks import *
>>> add.delay(4,5);taskA.delay();taskB.delay() #同时发起三个任务
<AsyncResult: 21408d7b-750d-4c88-9929-fee36b2f4474>
<AsyncResult: 737b9502-77b7-47a6-8182-8e91defb46e6>

celery -A myapp worker -l info  -Q default -P eventlet



<AsyncResult: 69b07d94-be8b-453d-9200-12b37a1ca5ab>
#也可以使用下面的方法调用task
>>> from myCeleryProj.app import app
>>> app.send_task(myCeleryProj.tasks.add,args=(4,5)
>>> app.send_task(myCeleryProj.tasks.taskA)
>>> app.send_task(myCeleryProj.tasks.taskB)

python app.py worker -Q  tasks_A,taks_B -l info
