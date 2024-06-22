# 프로젝트 문제 3번


from collections import deque

def problem3(input, N):
    """
    곰의 초기 위치를 찾고 초기 위치에서부터 곰이 이동할 수 있는 위치를 탐색하기 위해 bfs 함수를 호출
    bfs 함수를 이용해 벌집을 먹고 곰의 크기와 같은 수의 벌집을 먹을 때마다 곰의 크기를 1씩 증가시킴
    먹을 수 있는 벌집을 전부 먹은 경우 곰이 이동하며 소요된 시간을 반환
    """


    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0

    # forest 리스트 초기화
    forest = [row[:] for row in input]

    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0


    def bfs(x, y, size):
        """
        너비 우선 탐색으로 곰의 초기 위치에서부터 상하좌우로 탐색
        이동 가능한 위치를 큐에 추가하고 먹을 수 있는 벌집을 리스트에 추가
        먹을 수 있는 벌집의 위치와 벌집까지의 거리를 반환
        """


        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향
        visited = [[False] * N for _ in range(N)]  # 방문 여부
        queue = deque([(x, y, 0)])  # 초기 위치, 거리
        visited[x][y] = True
        edible_honeycombs = []

        while queue:
            cx, cy, dist = queue.popleft()  # deque를 활용하여 pop

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if forest[nx][ny] <= size:  # 이동 가능한 경우
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
                        if 0 < forest[nx][ny] < size:  # 먹을 수 있는 벌집인 경우
                            edible_honeycombs.append((dist + 1, nx, ny))

        return sorted(edible_honeycombs)[0] if edible_honeycombs else None

    while True:
        result = bfs(bear_x, bear_y, bear_size)

        if result is None:
            break
        
        # bfs로부터 먹을 수 있는 가장 가까운 벌집의 위치와 벌집까지의 거리를 받아 곰을 그곳에 위치시키고 해당 벌집 삭제
        dist, honey_x, honey_y = result
        time += dist
        bear_x, bear_y = honey_x, honey_y
        honeycomb_count += 1
        forest[honey_x][honey_y] = 0

        if honeycomb_count == bear_size:
            bear_size += 1  # 곰의 크기와 같은 수의 벌집을 먹을 때마다 곰의 크기가 1씩 증가
            honeycomb_count = 0

    return time


# 사용자로부터 숲의 크기와 상태 입력받기
while True:
    N = int(input("숲의 크기를 입력하세요: "))
    if 2 <= N <= 20:
        break
    else:  # 입력이 조건에 맞지 않는 경우
        print("숲의 크기는 2 이상 20 이하입니다.")

forest_input = []
print("숲의 상태를 입력하세요:")
for _ in range(N):
    row = list(map(int, input().split()))
    forest_input.append(row)


# 함수 실행 및 결과 출력
result = problem3(forest_input, N)

print(result)


