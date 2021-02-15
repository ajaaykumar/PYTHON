# Exercise Question 8: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list.

def main(nested_list,sub_list):
    
    for i in sub_list:
        nested_list[2][1][2].append(i)
    
    print(nested_list)



if __name__ == "__main__":
    
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]
    main(list1,sub_list)

