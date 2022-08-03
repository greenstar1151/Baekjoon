import sys

N, M = map(int, input().split())

testcase_in = sys.stdin.read().rstrip()
testcase_in = testcase_in.split('\n')
keywords = testcase_in[:N]
posts = testcase_in[N:]

keywords = set(keywords)
for post in posts:
    post_kw = set(post.split(','))
    keywords.difference_update(post_kw)
    print(len(keywords))
