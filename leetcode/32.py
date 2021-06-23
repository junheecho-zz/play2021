# leetcode 32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def f(s):
            def extract_parentheses(s):
                d = 0
                at = 0
                parentheses = 0
                valid = True

                if s=='': return False, 0, ''

                for i, c in enumerate(s):
                    if c=='(': 
                        d += 1
                    if c==')' and d > 0: 
                        d -= 1
                        parentheses += 2
                    if c==')' and d == 0:
                        valid = False
                        break

                return valid and d==0, parentheses, s[i+1:]

            valid, parentheses, s1 = extract_parentheses(s)
            print (valid, parentheses, s1)
            if valid:
                return parentheses + f(s1)
            else:
                rest = 0 if s1 == '' else f(s1)
                return max(parentheses, rest)

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