with open("day4_input.txt") as input_text:
    text = True
    total_sum = 0
    while text:
        match = None
        text = input_text.readline().strip("\n")
        stopp = False
        if text:
            word = text.split()
            # print (word, len (word))
            for i in range(len(word)-1):
                if stopp: break
                for j in range(i+1,len(word)):
                    # print (i,j)
                    wi = word[i]
                    wj = word[j]
                    if wj == wi:
                        total_sum += 1
                        # print(wi, wj)
                        match = True
                        stopp = True
                        break

    print(512 - total_sum)
