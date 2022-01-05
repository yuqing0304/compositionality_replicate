import numpy as np
import os


def read_a_log(file_path):
    '''Deal a file endding with .log. eg: log20220105_0.log'''
    with open(file_path, 'r') as f:
        lines = f.readlines()

    content = eval(lines[-2].rstrip()) # get the last line and transform it to dict object
    acc = content['uniform holdout']['acc']
    return acc


def process_dir(current_dir):
    '''process a directory. eg: grid(2,5)'''
    accs = []
    for log_file in sorted(os.listdir(current_dir)):
        file_path = os.path.join(current_dir, log_file)
        acc = read_a_log(file_path)
        accs.append(acc)
    acc_mean = np.mean(accs)
    acc_std = np.std(accs)
    acc_sem = acc_std / np.sqrt(10)
    return acc_mean, acc_sem


def main():
    res = {} 
    result_dir = "./results/"
    dir_list = os.listdir(result_dir)
    dir_list.sort(key = lambda x: int(x[:5]))
    for name in sorted(dir_list):
        tmp_dir = os.path.join(result_dir, name)
        acc_mean, acc_sem = process_dir(tmp_dir)
        tmp = {"acc_mean": acc_mean, "acc_sem": acc_sem}
        res[name] = tmp
        #print(f"{name} 'mean': {acc_mean} | 'sem': {acc_sem}")
    print(res)


if __name__ == "__main__":
    main()
