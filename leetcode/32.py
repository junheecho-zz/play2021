# leetcode 32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def f(s):
            pass
        ret = f(s)
        print(s, '=>', ret)
        return ret
if __name__ == '__main__':
    assert Solution().longestValidParentheses("()(())") == 6
    assert Solution().longestValidParentheses("(()))))") == 4
    assert Solution().longestValidParentheses("(()())") == 6
    assert Solution().longestValidParentheses("(()))(()())") == 6
    assert Solution().longestValidParentheses("(((()") == 2
    assert Solution().longestValidParentheses("(()(())") == 6
    assert Solution().longestValidParentheses("(()(()))") == 8
    assert Solution().longestValidParentheses("()(()") == 2
    
    assert Solution().longestValidParentheses("()())") == 4