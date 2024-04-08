l = ["ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__"]
new_l = []
for word in l:
    new_word = word.replace('_', ' ')
    new_l.append(new_word)
print(new_l)
