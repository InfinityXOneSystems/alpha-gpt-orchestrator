import threading

def spawn(target, args=()):
    t = threading.Thread(target=target, args=args, daemon=True)
    t.start()
    return t
