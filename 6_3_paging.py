# 6_3_paging.py

def getTotalPage(_TotalIssue, _MaxIssueCnt):
    MaxPageCnt = round(_TotalIssue / _MaxIssueCnt)
    print("%d개의 게시물을 한 페이지에 %d개씩 출력하면 총 %d개의 페이지가 필요합니다." % (_TotalIssue, _MaxIssueCnt, MaxPageCnt))

TotalIssue = int(input("게시물의 총 건수를 입력하세요:\n"))
MaxIssueCnt = int(input("한 페이지에 보여줄 게시물의 수를 입력하세요:\n"))
getTotalPage(TotalIssue, MaxIssueCnt)