def calculate_blast_cells(H, W, field):
    bomb_rows = set()
    bomb_cols = set()

    for i in range(H):
        for j in range(W):
            if field[i][j] == '#':
                bomb_rows.add(i)
                bomb_cols.add(j)

    return len(bomb_rows) * W + len(bomb_cols) * H - len(bomb_rows) * len(bomb_cols)

H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
print(calculate_blast_cells(H, W, field))