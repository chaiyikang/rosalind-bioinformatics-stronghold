def minDistance(word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[None] * (l2 + 1) for _ in range(l1 + 1)]
        # distance, s1, s2
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                # if i == 0 or j == 0:
                #     dp[i][j] = max(i, j)
                #     continue
                if i == 0:
                    dp[i][j] = (j, "-" * j, word2[:j])
                    continue
                if j == 0:
                    dp[i][j] = (i, word1[:i], "-" * i)
                    continue
                if word1[i - 1] == word2[j - 1]:
                    wish = dp[i - 1][j - 1]
                    dp[i][j] = (wish[0], wish[1] + word1[i - 1], wish[2] + word2[j - 1])
                else:
                    bestWishDistance = min(
                        dp[i][j - 1][0],
                        dp[i - 1][j][0],
                        dp[i - 1][j - 1][0]
                    )
                    if dp[i - 1][j - 1][0] == bestWishDistance:
                        # substitution at this char
                        wish = dp[i - 1][j - 1]
                        dp[i][j] = (bestWishDistance + 1, wish[1] + word1[i - 1], wish[2] + word2[j - 1])
                    elif dp[i - 1][j][0] == bestWishDistance:
                        # word1 deletion, put "-" in word2
                        wish = dp[i - 1][j]
                        dp[i][j] = (bestWishDistance + 1, wish[1] + word1[i - 1], wish[2] + "-")
                    elif dp[i][j - 1][0] == bestWishDistance:
                        # word1 addition, put "-" in word1
                        wish = dp[i][j - 1]
                        dp[i][j] = (bestWishDistance + 1, wish[1] + "-", wish[2] + word2[j - 1])

                    
                    
        for res in dp[l1][l2]:
            print(res)

from helpers import parse_fasta
def solution(input):
     s1, s2 = parse_fasta(input)[1]
     return minDistance(s1, s2)


solution('''>Rosalind_7964
EVLFSITFRMRWIVHMHATFTQWSQWYLLYWPPVLHTPEIIQRVYNTHNHWIARFMYVIP
KPKHEYEWYVETCHICHNHDDKSHMPFFAQDCEWVHCEHFNKCPPRNGTEIWWSMMHNWP
IYKLVRKRSTMGMPKEMCDIGWILPLARQDWHEGYPAACEFTHCCLDTFYTQKDTKLMIR
KREQLCQNNGDPWDSMQSTGPMDWVFICNWPKWDAYKPGLQNKCACWGGPMWCHCVRSMF
MITHECSSGAAILVATRDAYYMQFRKVVVQKIFEAYKGEKKHKRTWNKPNTDPYWDFNMK
AYYQKQQTIANCDWCNNYVIPYFMYVFILDTPIGAVIGILFAYVTLTMSTIGIKQWILDC
LVHLSCPCDDETELESYGCCSWIKKWSEIDWLAMTYWANFFIYVTMSTHMKFETLSQWKY
YIKLTLDVLFNDFDGVWCGPDVMNYGNSTWYPMMVADQMFCKLNDHDRNSHRLDWGVSSQ
TIFNCSGHDFPCKSISYRVMQGKCVEAPSDVGCSQPQDGQYCMQSYSIKFSKLDHADHGL
EQCPMIAKYGCEETRSTYYRHHYKKLDYEKPSWLDQSLYWWRHMPAMIHDNWAIHKIIPF
NAEHEVQRSALADNHEHPGHPGHNHYLYHMHLLAKSMWFSDIKPTDATLSSPQESTAESE
MIFDIFDQILWCQWAACFFEFSNGSWYWQGMWHQCTSHVNMPIPMWCLSLWYVQPRKSMK
FKSLWDKTNGDYRRNYPSVCFWEGAKYCSRVWVNWCRVSGLFLQNKHFLINNWPIDMTTE
QETRTYYLM
>Rosalind_4711
EVLFSITFRMRWIVFTKWGRFTSMHNGFRATFTQGTSQVNLLEYLDYWPPVLHTAEIIQR
VYQTHNVKHWIARHMYVIPIFPFPKHEYEKYVETCHIFNNHRNDKVHMPFCEWVHCEHFP
KCTEIWWSQMFNWPIYSHRGHLELVFKTSTMRMPKEMCDIGDWHEGYPAACSTQHPAIVH
CNSTPQHQTGLDTFYTQKDTKLMIRKREQLCQNMGDPWDSMQSTGPMDWVFIYDQEIKQG
MFWKPMLYAYKNKLACWGGPMWCHCVRSMCSSGAAQFRKVVVQKICRPSLSMPWAYCNAA
CPYKSEKKTSGTNHGTDPYWDHVTATGKQQTIANCDWCNNYVIPWYAKQRLFAYVTLTMS
TIGIKKWIHDCLVHLERPMPLCPCDDNTELESRGCCSWIKKWSEIDMDSPAFWYFFQLGC
RLPRENRCNTMVLHMKFETLSFWKYYIKLTLNVLFNDFDGVKCGGQVMNYGFSTWYPMMV
ADQMFCKLNDHDRNSHRLDWGVSDQTIFNCSPCKSISYRRWPFLYAWCPPVQQITDVGCS
HDGQLCIQLNKWSQKFHVQTVEGWKLDHADHGLWQCPMIRSTYYRHHYWYYSIVLKLQYE
FYGSLDQSRYWWRPRSPQFPSMIHDMPDKEMIFAEPTDCCLLVEHPGHPGHNHYLYHMPG
TFIKNHLDSHLASFRWFSDIAPTDATLSSKMIFDITDQIWWCQWAACFFEFSNPQGMWHC
PTSHICLPSKQEFKFKSLWDYIRPASTNGDYRRNYPSVCFWEGAKYCIRVRVNDCRVSGL
FLQNKHFLINNWPTMRRNDMTTEQETRTYYFM''')