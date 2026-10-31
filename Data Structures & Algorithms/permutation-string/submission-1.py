class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #find the character counts for s1 because that is what we are comparing with the sliding window of s2
        character_cnt={}
        for i in s1:
            character_cnt[i]=character_cnt.get(i,0)+1
        
        #sliding window
        window={}
        l=0
        for r in range(len(s2)):#moves the right pointer
            window[s2[r]]=window.get(s2[r],0)+1 #adding   the right pointer element to the counts in the sliding window
           #negative case 
            if r-l+1>len(s1):
            #remove the count from the window
                window[s2[l]]=window[s2[l]]-1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l+=1

            #positive case where the window length does match (but the characters dont match)
            if window==character_cnt:
                return True
        return False
