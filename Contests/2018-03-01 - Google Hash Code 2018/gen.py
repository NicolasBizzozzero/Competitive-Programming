# 301-316
##mach : 1-20

list = []


def gen():
    for k in range(300, 500, 100):
        for i in range(1, 17):
            for j in range(1, 21):
                if(j < 10):
                    list.append("ppti-14-" + str(k + i) + "-0" + str(j))
                else:
                    list.append("ppti-14-" + str(k + i) + "-" + str(j))

        file = open("machines_list.txt", "w")

        for z in range(len(list)):
            file.write(list[z] + "\n")
        file.close()


gen()
