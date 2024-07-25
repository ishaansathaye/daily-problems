from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''O(2^l) l is length of string'''
        '''For loop based recursion'''
        result = []
        self.helper(s, 0, [], result)
        return result

    # either pass the substring s or keep s and just move s
    def helper(self, s, pivot, path, result):
        # base
        if pivot == len(s):
            result.append(path.copy())
            return
        # logic
        for i in range(pivot, len(s)):
            currSub = s[pivot:i+1]
            # recurse on string after currSub if currSub is palindrome:
            if self.isPalindrome(currSub):
                # action
                path.append(currSub)
                # recurse
                self.helper(s, i+1, path, result)
                # backtrack
                path.pop(len(path)-1)

    def isPalindrome(self, s):
        '''O(n)'''
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


'''0/1 Recursion Java Solution:'''
# class Solution {
#     List<List<String>> result;
#     public List<List<String>> partition(String s) {
#         this.result = new ArrayList<>();
#         helper(s, 0, 0, new ArrayList<>(), 0);
#         return result;
#     }
#     private void helper(String s,int pivot, int i,
# List<String> path, int cnt){
#         // base
#         if(i == s.length()){
#             if(cnt == s.length()){
#                 result.add(new ArrayList<>(path));
#             }
#             return;
#         }
#         //logic
#          //dont choose
#         helper(s, pivot, i+1, path, cnt);
#         // choose
#         String currSub = s.substring(pivot, i+1);
#         if(isPalindrome(currSub)){
#             //action
#             path.add(currSub);
#
#             //recurse
#             helper(s, i+1, i+1, path, cnt + currSub.length());
#             //backtrack
#             path.remove(path.size() - 1);
#         }
#
#
#     }
#     private boolean isPalindrome(String s){
#         int start=0;
#         int end=s.length()-1;
#         while(start<end){
#             if(s.charAt(start)!=s.charAt(end))
#                 return false;
#             start++;
#             end--;
#         }
#         return true;
#     }
# }
