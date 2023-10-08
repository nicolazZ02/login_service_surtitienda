import multiprocessing

bind = '0.0.0.0:8000'
backlog = 2048

workers = 2
workers_class = 'uvicorn.workers.UvicornWorker'
worker_connections = 1000
timeout = 30
keepalive = 2


spew = False

daemon = False
raw_env = []
umask = 0
user = None
group = None
tmp_upload_dir = None

loglevel = 'info'

proc_name = 'info'

def post_fork(server, worker):
    server.log.info("worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    # TODO document why this method is empty
    pass
    
def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spawing workers")

def worker_int(worker):
    worker.server.log.info("worker received INT or QUIT signal")

    import threading,sys,traceback
    id2name = {th.ident: th.name for th in threading.enumerate()}
    code = []
    for thread_id, stack in sys._current_frames().items():
        code.append("\n %s(%d)" % (id2name.get(thread_id, ""), thread_id))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename, lineno, name))
            if line:
                code.append(" %s" % (line.strip()))
    worker.server.log.debug("\n".join(code))

def worker_abort(worker):
    worker.server.log.info("worker received SIGABRT signal")