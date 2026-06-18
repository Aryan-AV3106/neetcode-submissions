class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))+"@"+ word
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        idx = 0
        while idx < len(s):
            j = idx
            while s[j] != "@":
                j +=1
                
            length = int(s[idx:j])
            word = s[j+1:j+1+length]
            decoded_list.append(word)
            idx = j + 1 + length

        return decoded_list