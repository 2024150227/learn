import threading
import time

# 共享变量
count = 0
# 创建互斥锁
lock = threading.Lock()

def add_task(thread_id, loop_times):
    global count
    for _ in range(loop_times):
        # 1. 抢锁：获取锁，没抢到就阻塞等待
        lock.acquire()
        try:
            # 临界区：只有拿到锁才能执行
            temp = count
            time.sleep(0.0001)  # 放大线程切换冲突
            count = temp + 1
            print(f"线程{thread_id}执行，当前count={count}")
        finally:
            # 2. 释放锁，无论是否异常都必须释放
            lock.release()

if __name__ == "__main__":
    thread_num = 3
    loop_count = 5
    thread_list = []

    # 创建并启动线程
    for i in range(thread_num):
        t = threading.Thread(target=add_task, args=(i, loop_count))
        thread_list.append(t)
        t.start()

    # 等待所有线程执行完毕
    for t in thread_list:
        t.join()

    print(f"\n所有线程执行完成，最终count={count}")