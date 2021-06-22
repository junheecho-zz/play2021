# leetcode 32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pass
    
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