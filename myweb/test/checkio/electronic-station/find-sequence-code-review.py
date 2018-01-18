# coding:utf8


def checkio(matrix):
    lim, stp = len(matrix), [(0, 1), (1, 0), (1, 1), (1, -1)]

    def sc(pr, pc, tr, tc):
        nr, nc = pr + tr, pc + tc
        return sc(nr, nc, tr, tc) + 1 if 0 <= nr < lim and 0 <= nc < lim and \
                                         matrix[pr][pc] == matrix[nr][
                                             nc] else 0

    return any(
            any(sc(i, j, m, n) + sc(i, j, -m, -n) > 2 for m, n in stp) for i in
            range(lim) for j in range(lim))
