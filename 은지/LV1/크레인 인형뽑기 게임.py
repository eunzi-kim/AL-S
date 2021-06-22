def solution(board, moves):
    # 터트린 인형 개수 초기화
    answer = 0
    # N의 값
    N = len(board)
    # 바구니 초기화
    Basket = []
    # 목표 : 위에서부터 인형을 하나 뽑아서 바구니에 넣기
    for x in moves:
        # 인형 뽑아서 바구니에 넣기
        for i in range(N):
            if board[i][x-1] != 0:
                Basket.append(board[i][x-1])
                board[i][x-1] = 0
                break
        # 바구니에 같은 인형 2개이면 터트리기
        if len(Basket) > 1 and Basket[-1] == Basket[-2]:
            Basket.pop(-1)
            Basket.pop(-1)
            # 터트린 인형 더해주기
            answer += 2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))