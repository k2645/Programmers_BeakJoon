import sys
input = sys.stdin.readline

def surveillanceArea(cctv_location, directions):
    cctv_area = []
    for dx, dy in directions:
        x, y = cctv_location
        while True:
            x, y = x + dx, y + dy
            if 0 <= x < N and 0 <= y < M and office_map[x][y] != 6:
                if office_map[x][y] == 0:
                    cctv_area.append((x, y))
            else:
                break
    return cctv_area

def backtracking(start, cctv_area, cctv_list):
    global max_blind_spot
    cctv_type_directions = {
        1: [[(-1, 0)], [(0, -1)], [(1, 0)], [(0, 1)]],
        2: [[(1, 0), (-1, 0)],
            [(0, 1), (0, -1)]],
        3: [[(1, 0), (0, 1)],
            [(-1, 0), (0, 1)],
            [(-1, 0), (0, -1)],
            [(1, 0), (0, -1)]],
        4: [[(-1, 0), (0, -1), (1, 0)],
            [(-1, 0), (0, -1), (0, 1)],
            [(-1, 0), (1, 0), (0, 1)],
            [(0, -1), (1, 0), (0, 1)]],
        5: [[(-1, 0), (0, -1), (1, 0), (0, 1)]]
    }
    if len(cctv_list) == len(cctvs):
        watch_cnt = 0
        for i, j in set(cctv_area):
            if office_map[i][j] == 0:
                watch_cnt += 1
        if watch_cnt > max_blind_spot:
            max_blind_spot = watch_cnt
        return

    x, y, type = cctvs[start]
    for idx, directions in enumerate(cctv_type_directions[type]):
        surveillance = (x, y, idx)
        if surveillance in surveillance_area.keys():
            result = surveillance_area[surveillance]
        else:
            result = surveillanceArea((x, y), directions)
            surveillance_area[surveillance] = result
        cctv_list.append(cctvs[start])
        backtracking(start + 1, cctv_area + result, cctv_list)
        cctv_list.pop()

N, M = map(int, input().split())
office_map = [list(map(int, input().split())) for _ in range(N)]
cctvs = []
count_cctv_or_wall = 0
for i in range(N):
    for j in range(M):
        if 0 < office_map[i][j] < 6:
            cctvs.append((i, j, office_map[i][j]))
        if office_map[i][j] != 0:
            count_cctv_or_wall += 1

max_blind_spot = 0
surveillance_area = dict()
backtracking(0, [], [])
print(N * M - count_cctv_or_wall - max_blind_spot)
