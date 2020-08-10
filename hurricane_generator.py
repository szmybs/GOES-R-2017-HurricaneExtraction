import numpy as np
import os

# .\\IRMA\\Visible\\2017253
class HurricaneGenerator(object):
    def __init__(self):
        pass
    
    @classmethod
    def directory_downstream(self, root_path, white_list=None, black_list=None):
        if os.path.isdir(root_path) == False:
            return []

        if white_list is not None and black_list is not None:
            print("黑名单-白名单最多只能存在一种")
            return []

        dirs = sorted(os.listdir(root_path))
        sift = []

        for di in dirs:
            di_path = os.path.join(root_path, di)
            if os.path.isdir(di_path) == False:
                continue
            if black_list is not None:
                if di in black_list:
                    continue
            if white_list is not None:
                if di not in white_list:
                    continue
            sift.append(di_path)
        
        return sift

    @classmethod
    def one_dircetory_generator(self, data_path, read_data_func):
        datas = sorted(os.listdir(data_path))
        for data in datas:
            dp = os.path.join(data_path, data)
            #yield(dp)
            yield(read_data_func(dp))
    

def name_visibility_date_dir_generator(root_path, read_data_func):
    while True:
        name_dirs = HurricaneGenerator.directory_downstream(root_path)

        for name_dir in name_dirs:
            visibility_dirs = HurricaneGenerator.directory_downstream(name_dir, white_list=['Visible'])
            #visibility_dirs = HurricaneGenerator.directory_downstream(name_dir)

            for visibility_dir in visibility_dirs:
                date_dirs = HurricaneGenerator.directory_downstream(visibility_dir)

                for date_dir in date_dirs:
                    odg = HurricaneGenerator.one_dircetory_generator(date_dir, read_npy_hurricane_data)    #使用读取npy的内部函数
                    while True:
                        try:
                            hdg = next(odg)
                            yield(hdg)
                        except StopIteration:
                            break
    
    def read_npy_hurricane_data(file_path):
        return np.load(file_path)


if __name__ == "__main__":

    from extract import HurricaneExtraction

    root_path = ".\\Data\\NpyData\\"
    nvdd = name_visibility_date_dir_generator(root_path, HurricaneExtraction.read_extraction_data)

    for i in range(10):
        tmp = next(nvdd)
        print(tmp)



