class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#hello
        # length of word + # + word
        encoded_word = ""
        for word in strs:
            buffer = f"{len(word)}#{word}"
            encoded_word += buffer

        print(encoded_word)
        return encoded_word

    def decode(self, s: str) -> List[str]:
        # read num until # hit, then grab num amount of char into buffer -> list add
        res = []
        num = 0
        i = 0
        num_mode = True
        str_buf = ""

        while i < len(s):
            print(i, s[i])
            # print(f"num_mode = {num_mode}")
            if s[i] == "#":
                # print("here")
                num_mode = False
                i += 1

            if num_mode:
                num = num * 10 + int(s[i])
                i += 1
            else:
                # print(f"num: {num}")
                while num_mode is False and num > 0:
                    # print(f" inner. i = {i}")
                    str_buf += s[i]
                    num -= 1
                    i += 1
                num_mode = True
                res.append(str_buf)
                str_buf = ""

        return res





            

                
            

        return ["word"]