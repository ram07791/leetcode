class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        
        folder.sort()
        ans = [folder[0]]
        
        for f in folder[1:]:
            if not f.startswith(ans[-1] + "/"):
                ans.append(f)
                
        return ans

        