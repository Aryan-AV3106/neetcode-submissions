class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + "@" + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0 
        decoded_str =[]
        while i < len(s):
            j = i
            while s[j]!="@":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            i = j+1+length
            decoded_str.append(word)
        return decoded_str 