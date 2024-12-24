
def cal_total(exp):
    total=0
    for e in exp:
        total+=e
    return total

eswar_exp=[100,200,300]
sriram_exp=[200,400,500]

print("Eswar Total exp:",cal_total(eswar_exp))
print("Sriram Total exp:",cal_total(sriram_exp))
