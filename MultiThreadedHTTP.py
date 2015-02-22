__author__ = 'steven'
import requests
import queue
import threading
import helper.Logger

class MultiThreadedHTTP():

    def __init__(self):
        self.log = helper.Logger.Logger()

    def worker(self, q, callback):
        q_filled = True
        while q_filled:
            try:
                Id = q.get(False)
                callback(**Id)

            except queue.Empty:
                q_filled = False

    def ExecuteCallsFromList(self, task_list, callback):
        """
        """
        q = queue.Queue()

        for item in task_list:  #iterate over the file one line at a time (memory efficient)
            self.log.debug(item)
            q.put(item)

        thread_count = 16
        for i in range(thread_count):
            t = threading.Thread(target=self.worker, args=(q, callback))
            t.start()
        #make the main thread wait till all the threads are done
        for t in threading.enumerate():
            if t is not threading.currentThread():
                t.join()

    def DoCall(self, method, url="", body="", header={}):
        print(method)
        print(url)
        r = requests.Response

        if method == "GET":
            r = requests.get(url=url, headers=header)

        if method == "PUT":
            r = requests.put(url=url, headers=header, body=body)
        print(r)
        print(type(r))
        print(r.status_code)

if __name__ == '__main__':
    caller = MultiThreadedHTTP()
    caller.DoCall(method="GET", url="http://127.0.0.1", header={"User-agent":"Test UA"})
    list = []
    for i in range(1000):
        list.append({"method":"GET", "url":"http://127.0.0.1/{0}".format(i), "header":{'User-agent': "UA{0}".format(i)}})

    caller.ExecuteCallsFromList(task_list=list, callback=caller.DoCall)



