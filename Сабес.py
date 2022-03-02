from contextlib import contextmanager

class Test:

    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f"Файл открыт, и добавлен материал {args}")
        self.opened = True

    def close(self):
        print(f"Файл закрыт")
        self.opened = False

    def __del__(self):
        if self.opened:
            print("Вы не закрыли файл!")

    def action(self):
        print("записали, что-то  в файл")

@contextmanager
def context(*args):
    resource = None
    try:
        resource = Test()
        resource.open(*args)
        yield resource
    except Exception:
        raise
    finally:
        if resource:
            resource.close()


if __name__ == "__main__":
    with context("test") as test:
        test.action()
