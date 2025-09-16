class Counter:
    # 클래스 변수 (모든 인스턴스가 공유)
    class_count = 0

    def __init__(self):
        # 인스턴스 변수 (각 인스턴스마다 별도)
        self.instance_count = 0
        Counter.class_count += 1

    def increment(self):
        self.instance_count += 1

# 예제 실행
if __name__ == "__main__":
    # 인스턴스 생성
    print("=== 클래스 변수와 인스턴스 변수 비교 ===")
    a = Counter()
    b = Counter()

    print("\n1. 초기 상태:")
    print(f"a의 instance_count: {a.instance_count}")
    print(f"b의 instance_count: {b.instance_count}")
    print(f"클래스 변수 class_count: {Counter.class_count}")

    print("\n2. a 인스턴스의 카운터 2회 증가:")
    a.increment()
    a.increment()
    print(f"a의 instance_count: {a.instance_count}")
    print(f"b의 instance_count: {b.instance_count}")
    print(f"클래스 변수 class_count: {Counter.class_count}")

    print("\n3. b 인스턴스의 카운터 1회 증가:")
    b.increment()
    print(f"a의 instance_count: {a.instance_count}")
    print(f"b의 instance_count: {b.instance_count}")
    print(f"클래스 변수 class_count: {Counter.class_count}")
