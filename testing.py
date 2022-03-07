from collections import Counter
bin_result_list = ['a','a','b']

def time_decaying(result_list):
    importance_granular = 1/len(result_list)
    result_decaying_dict = {}

    for s in set(result_list):
        result_decaying_dict[s] =0
    
    previous_importance = 0
    latest_label = 0
    for r in result_list:
        current_importance = previous_importance+importance_granular
        result_decaying_dict[r] += current_importance

        previous_importance = current_importance
        latest_label = r
    
    sorted_result_dict = sorted(result_decaying_dict.items(), key= (lambda x:x[1]),reverse=True)
    if sorted_result_dict[0][1] == sorted_result_dict[1][1]:
        label = latest_label

    else:
        label = sorted_result_dict[0][0]
    return label
    
# t = sorted(Counter(bin_result_list).items(),key = (lambda x:x[1]),reverse=True)[0][0] 

print(time_decaying(bin_result_list))